import unittest

from text_utils import compact


class CompactTests(unittest.TestCase):
    def test_mixed_whitespace(self):
        self.assertEqual(compact(" \t alpha  \tbeta\n\ngamma\r\n delta \t\n"), "alpha beta gamma delta")

    def test_empty_and_whitespace_only(self):
        for text in ("", " ", "\t\n\r", " \t\n\r\v\f ", "\u00a0\u2003\u2028"):
            with self.subTest(text=text):
                self.assertEqual(compact(text), "")

    def test_unicode_whitespace(self):
        self.assertEqual(compact("\u00a0alpha\u2003\u2028beta\u3000"), "alpha beta")

    def test_already_compact_text(self):
        for text in ("alpha", "alpha beta gamma", "Hello, 世界!"):
            with self.subTest(text=text):
                self.assertEqual(compact(text), text)

    def test_preserves_non_whitespace_characters(self):
        self.assertEqual(compact("  café\t世界!  a-b_c  "), "café 世界! a-b_c")


if __name__ == "__main__":
    unittest.main()
