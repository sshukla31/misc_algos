"""
Implement a trie with insert, search, starts_with, suggestions methods.
"""

from collections import defaultdict


class Trie:
    """
    Define methods for Trie data structure
    """
    def __init__(self):
        """ Initialize """
        self.root = defaultdict()

    def insert(self, word):
        """
        Inserts a new word into the trie.
        Args:
            word(string): A new word to be inserted in Trie
        Returns:
            void
        Raises:
            None
        """
        current = self.root
        for letter in word:
            current = current.setdefault(letter, {})

        current.setdefault("\0")

    def search(self, word):
        """
        Search a word within Trie
        Args:
            word(string): A word to be searched
        Returns:
            boolean:
                True if word in the trie else False
        Raises:
            None
        """
        current = self.root
        for letter in word:
            if letter in current:
                current = current[letter]
            else:
                return False

        return True if "\0" in current else False

    def starts_with(self, prefix):
        """
        Check if there is any word in the trie with given prefix.
        Args:
            prefix(string): Prefix to be matched within trie
        Returns:
            boolean:
                True if prefix match in the trie else False
        Raises:
            None
        """
        current = self.root
        for letter in prefix:
            if letter in current:
                current = current[letter]
            else:
                return False

        return True

    def suggestions(self, prefix):
        """
        Get all the words matching the prefix.
        eg: If 'main', 'mat' and 'met' are inserted and suggestions('ma')
            is passed, the result should be ['main', 'mat']
        Args:
            prefix(string): Prefix to be matched within trie and return words
        Returns:
            words(list): List of string matching the prefix
        Raises:
            None
        """
        current = self.root
        words = []
        _word = ""
        for char in prefix:
            if char in current:
                _word = "".join((_word, char))
                current = current[char]
            else:
                return []

        def _construct(data_dict, word):
            '''
            Recursive function to concatenate characters to the prefix to
            generate all possible word combinations that starts with prefix.
            Args:
                data_dict(dict): Dict of chars
                word(str): prefix of the word to be searched for
            eg: word = 'ab'
            data_dict = {'a': {
                'b': {
                    'c': {'\0': None},
                    's': {'\0': None}
                }
              }
            }
            Returns:
                words(list): List of all possible words starting with prefix.
                             eg: output -> ['abc', 'abs']
            '''
            for key, value in data_dict.iteritems():
                if key == '\0':
                    words.append(word)
                else:
                    _construct(
                        data_dict=data_dict[key],
                        word="".join((word, key))
                    )
            return words

        return _construct(data_dict=current, word=_word)


def main():
    """ Main """
    trie = Trie()
    words = [
        'man',
        'main',
        'matter',
        'maternal',
        'matter port',
        'men',
        'saturday',
        'saturn'
    ]
    for word in words:
        trie.insert(word)

    print trie.starts_with('ma')
    print trie.suggestions('ma')
    print trie.suggestions('sa')


if __name__ == '__main__':
    main()
