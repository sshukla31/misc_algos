""" Test case for trie.py module """

import unittest

from trie import Trie


class TrieTestCase(unittest.TestCase):
    """ Define test cases for Trie class """
    def setUp(self):
        """ Setup env before each test """
        self.trie = Trie()

    def tearDown(self):
        """ Tear down env after each test """
        pass

    def test_insert(self):
        """
        Test insert of the trie and assert if the
        word was added successfully
        """
        word = "bar"
        self.trie.insert(word)
        expected_result = [word]
        actual_result = self.trie.suggestions(word)
        self.assertEqual(expected_result, actual_result)

    def test_suggestion_when_prefix_valid(self):
        """
        Test suggestions of the trie and assert if all the word
        mathcing the prefix are returned. There should be 2 matching
        words for a prefix 'bar'
        """
        words = ["bar", "barcelona", "foo", "foobar"]
        valid_key = "bar"
        for word in words:
            self.trie.insert(word)

        expected_result = ["bar", "barcelona"]
        actual_result = self.trie.suggestions(valid_key)
        self.assertEqual(expected_result, actual_result)

    def test_suggestion_when_prefix_invalid(self):
        """
        Test suggestions of the trie and assert if all the word
        mathcing the prefix are returned. There should be no matching
        words for a prefix 'foo'
        """
        words = ["bar", "barcelona"]
        invalid_key = "foo"
        for word in words:
            self.trie.insert(word)

        expected_result = []
        actual_result = [invalid_key] \
            if invalid_key in self.trie.suggestions(invalid_key) else []
        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    """ main() """
    unittest.main()
