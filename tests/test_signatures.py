import unittest

from hixbrain import signatures as sig
from hixbrain.collect import _keyword_passages, slug_candidates, summarize_jobs


class DetectVendorsTest(unittest.TestCase):
    def test_detects_script_urls(self):
        html = '<script src="https://apps.mypurecloud.com/widgets/9.0/cxbus.min.js"></script>' \
               '<script src="https://service.force.com/embeddedservice/5.0/esw.min.js"></script>'
        hits = sig.detect_vendors(html)
        self.assertEqual(hits["Genesys"], "ccaas")
        self.assertEqual(hits["Salesforce Service Cloud"], "crm")

    def test_short_tokens_need_word_boundaries(self):
        self.assertNotIn("8x8", sig.detect_vendors("grid-template: 18x80px"))
        self.assertIn("8x8", sig.detect_vendors("We run 8x8 for phones"))
        self.assertNotIn("TTEC", sig.detect_vendors("attecting"))

    def test_no_false_positive_on_plain_text(self):
        self.assertEqual(sig.detect_vendors("We sell shoes online."), {})


class ClassifyTitleTest(unittest.TestCase):
    def test_buckets(self):
        cases = {
            "Customer Service Representative - Remote": "frontline_agent",
            "Bilingual Call Center Agent": "frontline_agent",
            "VP, Customer Experience": "cx_leadership",
            "Director of Contact Center Operations": "cx_leadership",
            "Workforce Management Analyst": "contact_center_ops",
            "Genesys Cloud Engineer": "contact_center_ops",
            "Conversational AI Designer": "conversational_ai",
            "IVR Developer": "conversational_ai",
            "Salesforce Service Cloud Administrator": "crm_platform",
            "Senior Machine Learning Engineer": "ai_data",
            "Accountant": None,
        }
        for title, bucket in cases.items():
            with self.subTest(title=title):
                self.assertEqual(sig.classify_title(title), bucket)

    def test_summarize_counts(self):
        jobs = [{"title": t} for t in ["Call Center Agent", "Call Center Agent", "IVR Developer", "Accountant"]]
        s = summarize_jobs(jobs)
        self.assertEqual(s["total_open_roles"], 4)
        self.assertEqual(s["bucket_counts"], {"frontline_agent": 2, "conversational_ai": 1})


class PhoneTest(unittest.TestCase):
    def test_toll_free_vs_local(self):
        toll, other = sig.find_phone_numbers("Call 1-800-221-1212 or (404) 715-2600 or 888.555.0100")
        self.assertEqual(toll, {"8002211212", "8885550100"})
        self.assertEqual(other, {"4047152600"})


class HelpersTest(unittest.TestCase):
    def test_slug_candidates(self):
        self.assertEqual(slug_candidates("delta.com", "Delta Air Lines"), ["delta", "deltaairlines"])

    def test_keyword_passages(self):
        text = "We operate a large contact center. " * 3
        out = _keyword_passages(text, ["contact center", "missing"], per_kw=2, width=20)
        self.assertIn("contact center", out)
        self.assertNotIn("missing", out)


if __name__ == "__main__":
    unittest.main()
