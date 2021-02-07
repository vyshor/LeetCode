class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        self.max_size = 0

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        curr_node = self.root
        for i, c in enumerate(word):
            if not curr_node.get(c):
                curr_node[c] = {}
                if i == len(word) - 1:
                    curr_node[c]['-'] = True
                else:
                    curr_node = curr_node[c]
                    continue
            else:
                curr_node = curr_node[c]
        self.max_size = max(self.max_size, len(word))
        # print(self.root)

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        if len(word) > self.max_size:
            return False
        curr_node = self.root

        def deep_search(word, curr_node):
            # print(curr_node)
            if word == '':
                return curr_node.get('-', False)
            elif word[0] == '.':
                return any([deep_search(word[1:], curr_node[k]) if k != '-' else False for k in curr_node])
            else:
                return deep_search(word[1:], curr_node[word[0]]) if curr_node.get(word[0]) else False

        return deep_search(word, curr_node)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

# Time: O(n) for n length of word for adding, O(26^n) for searching if all are '.'
# Space: O(26^n) for n length of word

# Runtime: 460 ms, faster than 17.32% of Python3 online submissions for Add and Search Word - Data structure design.
# Memory Usage: 24.4 MB, less than 21.74% of Python3 online submissions for Add and Search Word - Data structure design.
