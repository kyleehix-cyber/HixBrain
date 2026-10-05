import unittest

try:
    from hixbrain.render_pdf import build_html, md_to_html
except ImportError:  # markdown not installed
    md_to_html = None


@unittest.skipIf(md_to_html is None, "pip install markdown")
class RenderTest(unittest.TestCase):
    def test_hypothesis_badge_not_duplicated(self):
        out = md_to_html("*🧠 Hypothesis:* they need help")
        self.assertEqual(out.count("Hypothesis"), 1)
        self.assertIn('class="badge hyp"', out)

    def test_bare_urls_become_links_without_double_wrapping(self):
        out = md_to_html("1. Src — https://example.com/a · [x](https://example.com/b)")
        self.assertIn('href="https://example.com/a"', out)
        self.assertIn('href="https://example.com/b"', out)

    def test_tables_and_internal_banner(self):
        import tempfile, os
        with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False) as f:
            f.write("| a | b |\n|---|---|\n| 1 | 2 |\n")
        try:
            doc = build_html([f.name], "T", internal=True)
        finally:
            os.unlink(f.name)
        self.assertIn("<table>", doc)
        self.assertIn("INTERNAL", doc)


if __name__ == "__main__":
    unittest.main()
