import unittest
import merge_sort

class MergeSortTest(unittest.TestCase):

    def test_merge_list(self):
        actual_list = [99, 1, 6, 4, 0, 77, -1]
        result = merge_sort.merge_sort(actual_list)
        self.assertEqual(sorted(actual_list), result)


if __name__ == '__main__':
    unittest.main()
