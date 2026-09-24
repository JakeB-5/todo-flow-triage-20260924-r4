import unittest

from sequence_utils import ordered_unique


class OrderedUniqueTests(unittest.TestCase):
    def test_interleaved_duplicates_preserve_first_occurrence_order(self):
        self.assertEqual(ordered_unique([3, 1, 3, 2, 1, 4, 2]), [3, 1, 2, 4])

    def test_empty_input(self):
        self.assertEqual(ordered_unique([]), [])

    def test_unique_input_returns_independent_list(self):
        values = ['c', 'a', 'b']
        result = ordered_unique(values)
        self.assertEqual(result, ['c', 'a', 'b'])
        self.assertIsNot(result, values)
        self.assertEqual(values, ['c', 'a', 'b'])

    def test_input_with_duplicates_is_unchanged(self):
        values = ['b', 'a', 'b', 'c', 'a']
        original = values.copy()
        self.assertEqual(ordered_unique(values), ['b', 'a', 'c'])
        self.assertEqual(values, original)

    def test_generator_input(self):
        values = (value for value in [5, 2, 5, 1, 2])
        self.assertEqual(ordered_unique(values), [5, 2, 1])

    def test_hashable_values_and_equal_values(self):
        first = (1, 2)
        equal = tuple([1, 2])
        result = ordered_unique([first, None, equal, 'x', None])
        self.assertEqual(result, [(1, 2), None, 'x'])
        self.assertIs(result[0], first)


if __name__ == '__main__':
    unittest.main()
