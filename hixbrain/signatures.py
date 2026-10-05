"""Signal dictionaries for detecting a prospect's CX / contact-center stack and
classifying what their job postings reveal. Pure data + pure functions so they
can be unit tested offline."""

import re

# Vendor -> (category, substrings that appear in page HTML / script URLs / job text).
# Matching is case-insensitive substring search.
VENDORS = {
    # CRM / service desks (integration targets)
    "Salesforce Service Cloud": ("crm", ["salesforceliveagent", "embeddedservice", "force.com", "my.site.com", "messaging.salesforce", "service cloud", "salesforce"]),
    "ServiceNow": ("crm", ["service-now.com", "servicenow"]),
    "Microsoft Dynamics 365": ("crm", ["dynamics.com", "omnichannelengagementhub", "dynamics 365", "d365"]),
    "Zendesk": ("crm", ["zdassets.com", "zendesk"]),
    "Oracle Service Cloud": ("crm", ["custhelp.com", "rightnow", "oracle service cloud"]),
    "HubSpot": ("crm", ["hs-scripts.com", "hubspot"]),
    "Freshworks": ("crm", ["freshchat", "freshdesk", "freshworks"]),
    "Kustomer": ("crm", ["kustomer"]),
    "Gladly": ("crm", ["gladly"]),
    "Epic (healthcare)": ("crm", ["epic systems", "mychart"]),
    # Contact-center platforms (CCaaS / on-prem)
    "Genesys": ("ccaas", ["genesys", "purecloud", "mypurecloud", "inindca"]),
    "NICE CXone": ("ccaas", ["niceincontact", "nice-incontact", "cxone", "brandembassy", "nice inContact"]),
    "Five9": ("ccaas", ["five9"]),
    "Talkdesk": ("ccaas", ["talkdesk"]),
    "Amazon Connect": ("ccaas", ["amazon connect", "amazon-connect", "my.connect.aws", "connect-chat"]),
    "Twilio Flex": ("ccaas", ["twilio"]),
    "Avaya": ("ccaas", ["avaya"]),
    "Cisco Webex Contact Center": ("ccaas", ["webex contact center", "cisco uccx", "cisco ucce", "cisco contact center"]),
    "RingCentral": ("ccaas", ["ringcentral"]),
    "8x8": ("ccaas", ["8x8"]),
    "Vonage": ("ccaas", ["vonage"]),
    "Verint": ("ccaas", ["verint"]),
    # Conversational AI / chat / IVA — competitors or incumbents
    "Nuance (Microsoft)": ("conversational_ai", ["nuance", "touchcommerce"]),
    "LivePerson": ("conversational_ai", ["liveperson", "lpcdn", "lpsnmedia"]),
    "Google CCAI / Dialogflow": ("conversational_ai", ["dialogflow", "contact center ai", "ccai"]),
    "Amazon Lex": ("conversational_ai", ["amazon lex"]),
    "IBM watsonx Assistant": ("conversational_ai", ["watsonplatform", "watson assistant", "watsonx"]),
    "Kore.ai": ("conversational_ai", ["kore.ai"]),
    "Cognigy (NICE)": ("conversational_ai", ["cognigy"]),
    "PolyAI": ("conversational_ai", ["polyai", "poly.ai"]),
    "Parloa": ("conversational_ai", ["parloa"]),
    "Sierra": ("conversational_ai", ["sierra.ai"]),
    "Decagon": ("conversational_ai", ["decagon"]),
    "Ada": ("conversational_ai", ["ada.support", "ada.cx"]),
    "Yellow.ai": ("conversational_ai", ["yellow.ai", "yellowmessenger"]),
    "Replicant": ("conversational_ai", ["replicant"]),
    "SoundHound / Amelia": ("conversational_ai", ["soundhound", "amelia.ai"]),
    "ASAPP": ("conversational_ai", ["asapp"]),
    "Uniphore": ("conversational_ai", ["uniphore"]),
    "Observe.AI": ("conversational_ai", ["observe.ai"]),
    "Intercom": ("conversational_ai", ["intercom.io", "widget.intercom", "intercomcdn"]),
    "Drift / Salesloft": ("conversational_ai", ["js.driftt.com", "drift.com"]),
    "Glia": ("conversational_ai", ["glia.com", "salemove"]),
    "Sprinklr": ("conversational_ai", ["sprinklr"]),
    "[24]7.ai": ("conversational_ai", ["247.ai", "247-inc"]),
    "Khoros": ("conversational_ai", ["khoros", "lithium.com"]),
    # Speech / voice-agent infrastructure (Deepgram and its direct competitors)
    "Deepgram": ("speech_ai", ["deepgram"]),
    "AssemblyAI": ("speech_ai", ["assemblyai"]),
    "ElevenLabs": ("speech_ai", ["elevenlabs"]),
    "Speechmatics": ("speech_ai", ["speechmatics"]),
    "Cartesia": ("speech_ai", ["cartesia"]),
    "Rev.ai": ("speech_ai", ["rev.ai"]),
    "Soniox": ("speech_ai", ["soniox"]),
    "Gladia": ("speech_ai", ["gladia"]),
    "AWS Transcribe": ("speech_ai", ["amazon transcribe", "aws transcribe"]),
    "Azure Speech": ("speech_ai", ["azure speech", "azure cognitive services speech", "cognitiveservices"]),
    "Google Speech-to-Text": ("speech_ai", ["google speech-to-text", "cloud speech-to-text", "google stt"]),
    "OpenAI Whisper / Realtime": ("speech_ai", ["whisper", "openai realtime", "realtime api"]),
    "Vapi": ("conversational_ai", ["vapi.ai", "vapi"]),
    "Retell AI": ("conversational_ai", ["retellai", "retell ai"]),
    "Bland AI": ("conversational_ai", ["bland.ai", "bland ai"]),
    # Voice of customer / analytics
    "Qualtrics": ("voc", ["qualtrics"]),
    "Medallia": ("voc", ["medallia", "kampyle"]),
    # Outsourced contact center (BPO)
    "Teleperformance": ("bpo", ["teleperformance"]),
    "Concentrix": ("bpo", ["concentrix"]),
    "TTEC": ("bpo", ["ttec"]),
    "Alorica": ("bpo", ["alorica"]),
    "Foundever / Sitel": ("bpo", ["foundever", "sitel"]),
    "TaskUs": ("bpo", ["taskus"]),
}

# Short or ambiguous tokens that need word boundaries to avoid false hits
# ("8x8" in a CSS grid, "ttec" inside other words, "ada" etc.).
_WORD_BOUNDARY = {"vapi", "whisper", "cartesia", "gladia", "8x8", "ttec", "ccai", "d365", "asapp", "sitel", "replicant", "nuance", "decagon", "parloa", "verint", "avaya"}


def _contains(text_lower, needle):
    needle = needle.lower()
    if needle in _WORD_BOUNDARY:
        return re.search(r"(?<![a-z0-9])" + re.escape(needle) + r"(?![a-z0-9])", text_lower) is not None
    return needle in text_lower


def detect_vendors(text):
    """Return {vendor: category} for every vendor whose signature appears in text."""
    low = text.lower()
    hits = {}
    for vendor, (category, needles) in VENDORS.items():
        if any(_contains(low, n) for n in needles):
            hits[vendor] = category
    return hits


# Job-title buckets. Order matters: first matching bucket wins.
JOB_BUCKETS = [
    ("conversational_ai", r"conversational|virtual agent|voice agent|speech recognition|\basr\b|text.to.speech|\btts\b|\bivr\b|\bivas?\b|voice (ai|bot|assistant|experience)|chatbot|\bnlu\b|\bnlp\b|dialog(ue)? design|speech"),
    ("cx_leadership", r"(chief|vp|vice president|head|director|sr\.? director).{0,40}(customer|experience|\bcx\b|contact cent|call cent|care|service operations|member services|patient access)"),
    ("contact_center_ops", r"workforce management|\bwfm\b|contact cent(er|re).{0,30}(manager|supervisor|analyst|lead|engineer|architect)|call cent(er|re).{0,30}(manager|supervisor|analyst|lead)|quality assurance.{0,20}(analyst|specialist)|telephony|genesys|five9|amazon connect|nice cxone|\bcti\b"),
    ("crm_platform", r"salesforce|servicenow|service now|dynamics 365|zendesk|\bcrm\b"),
    ("frontline_agent", r"customer (service|care|support|success) (rep|representative|agent|associate|specialist|advocate)|call cent(er|re)|contact cent(er|re)|member services|patient access|reservations? (agent|sales)|customer care|bilingual.{0,30}(rep|agent|representative)|claims (rep|representative|associate)|collections (rep|agent|specialist)|help ?desk|service desk"),
    ("ai_data", r"machine learning|\bml\b|\bai\b|artificial intelligence|data scien|\bllm\b|generative"),
]


def classify_title(title):
    t = title.lower()
    for bucket, pattern in JOB_BUCKETS:
        if re.search(pattern, t):
            return bucket
    return None


# Phrases worth quoting from 10-K / 10-Q / earnings text for a Voice AI seller.
FILING_KEYWORDS = [
    "contact center", "call center", "customer service", "customer care", "customer experience",
    "call volume", "hold time", "wait time", "self-service", "digital channels", "cost to serve",
    "artificial intelligence", "generative ai", "automation", "chatbot", "virtual assistant",
    "outsourc", "service providers", "workforce", "attrition", "net promoter",
]

TOLL_FREE = re.compile(r"(?:\+?1[\s.\-]?)?\(?8(00|33|44|55|66|77|88)\)?[\s.\-]?\d{3}[\s.\-]?\d{4}")
PHONE = re.compile(r"(?:\+?1[\s.\-]?)?\(?[2-9]\d{2}\)?[\s.\-]\d{3}[\s.\-]\d{4}")


def find_phone_numbers(text):
    """Return (toll_free, other) sets of normalized 10-digit numbers."""
    def norm(m):
        digits = re.sub(r"\D", "", m)
        return digits[-10:]
    toll = {norm(m.group(0)) for m in TOLL_FREE.finditer(text)}
    other = {norm(m.group(0)) for m in PHONE.finditer(text)} - toll
    return toll, other
