class Node:
    def __init__(self):
        self.route = {}
        self.end = False

    def add(self, word, idx):
        if len(word) == idx:
            self.end = True
            return

        c = word[idx]
        if c not in self.route:
            self.route[c] = Node()
        self.route[c].add(word, idx+1)

    def find(self, word, idx):
        if len(word) == idx:
            return len(word)

        c = word[idx]
        if c not in self.route:
            return idx
        return self.route[c].find(word, idx+1)

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        trie = Node()
        for word in arr1:
            word = str(word)
            trie.add(word, 0)

        maxx = 0
        for word in arr2:
            word = str(word)
            maxx = max(maxx, trie.find(word, 0))
        return maxx
