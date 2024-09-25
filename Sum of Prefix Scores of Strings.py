class Node:
    def __init__(self):
        self.route = {}
        self.score = 0

    def add(self, word, idx):
        if len(word) == idx:
            return

        c = word[idx]
        if c not in self.route:
            self.route[c] = Node()
        self.route[c].score += 1
        self.route[c].add(word, idx+1)

    def find(self, word, idx):
        if len(word) == idx:
            return self.score

        c = word[idx]
        if c not in self.route:
            return self.score
        return self.score + self.route[c].find(word, idx+1)

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Node()
        for word in words:
            trie.add(word, 0)

        arr = []
        for word in words:
            arr.append(trie.find(word, 0))
        return arr
