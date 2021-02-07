class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        self.max_size = 0

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
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
            elif i == len(word) - 1:
                curr_node[c]['-'] = True
            else:
                curr_node = curr_node[c]
        self.max_size = max(self.max_size, len(word))

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        if len(word) > self.max_size:
            return False
        curr_node = self.root

        def deep_search(word, curr_node):
            # print(curr_node)
            if word == '':
                return curr_node.get('-', False)
            else:
                return deep_search(word[1:], curr_node[word[0]]) if curr_node.get(word[0]) else False

        return deep_search(word, curr_node)

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        if len(prefix) > self.max_size:
            return False
        curr_node = self.root

        def deep_search(word, curr_node):
            # print(curr_node)
            if word == '':
                return len(curr_node) > 0
            else:
                return deep_search(word[1:], curr_node[word[0]]) if curr_node.get(word[0]) else False

        return deep_search(prefix, curr_node)

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

# Time: O(n) for insert for n length of characters, O(n) for search, O(n) for prefix
# Space: O(xn) for x number of different words of max characters n

# Runtime: 192 ms, faster than 68.56% of Python3 online submissions for Implement Trie (Prefix Tree).
# Memory Usage: 28.5 MB, less than 62.96% of Python3 online submissions for Implement Trie (Prefix Tree).