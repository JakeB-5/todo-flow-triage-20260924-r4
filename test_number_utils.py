import unittest

from number_utils import safe_divide


class SafeDivideTests(unittest.TestCase):
    def test_nonzero_division(self):
        for numerator, denominator, expected in (
            (7, 2, 3.5),
            (-7, 2, -3.5),
            (7, -2, -3.5),
            (-7, -2, 3.5),
            (0, 2, 0.0),
        ):
            with self.subTest(numerator=numerator, denominator=denominator):
                self.assertEqual(safe_divide(numerator, denominator), expected)

    def test_zero_denominator_defaults_to_none(self):
        for denominator in (0, 0.0, -0.0):
            with self.subTest(denominator=denominator):
                self.assertIsNone(safe_divide(5, denominator))

    def test_zero_denominator_returns_exact_fallback(self):
        for fallback in (object(), 0, False, "unavailable", None):
            with self.subTest(fallback=fallback):
                self.assertIs(safe_divide(5, 0, fallback), fallback)

    def test_nonzero_denominator_ignores_fallback(self):
        self.assertEqual(safe_divide(9, 2, fallback="unused"), 4.5)

    def test_invalid_operands_raise_type_error(self):
        for numerator, denominator in (("invalid", 2), (2, "invalid"), (2, None)):
            with self.subTest(numerator=numerator, denominator=denominator):
                with self.assertRaises(TypeError):
                    safe_divide(numerator, denominator, fallback="unused")

    def test_division_error_propagates_unchanged(self):
        error = RuntimeError("division failed")

        class FailingNumerator:
            def __truediv__(self, denominator):
                raise error

        with self.assertRaises(RuntimeError) as caught:
            safe_divide(FailingNumerator(), 2, fallback="unused")
        self.assertIs(caught.exception, error)


if __name__ == "__main__":
    unittest.main()
