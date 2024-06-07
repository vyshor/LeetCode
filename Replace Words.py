class Trie:
    def __init__(self, is_word=False):
        self.is_word = is_word
        self.paths = {}

    def add(self, i, word):
        if i == len(word):
            self.is_word = True
            return

        c = word[i]
        if c not in self.paths:
            self.paths[c] = Trie()
        self.paths[c].add(i+1, word)

    def search(self, i, word):
        if self.is_word:
            return word[:i]

        if i == len(word) or word[i] not in self.paths:
            return ""

        return self.paths[word[i]].search(i+1, word)

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        root = Trie()
        for word in dictionary:
            root.add(0, word)

        ans = []
        words = sentence.split(' ')
        for word in words:
            valid_word = root.search(0, word)
            if valid_word:
                ans.append(valid_word)
            else:
                ans.append(word)
        return ' '.join(ans)

