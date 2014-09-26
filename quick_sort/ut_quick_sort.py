import unittest
import quick_sort

class QuickSortTest(unittest.TestCase):

    def test_merge_list(self):
        actual_list = [99, 1, 6, 4, 0, 77, -1]
        result = quick_sort.quick_sort(actual_list, 0 , len(actual_list) - 1)
        self.assertEqual(sorted(actual_list), result)


if __name__ == '__main__':
    unittest.main()
