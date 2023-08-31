class Node:
    def __init__(self, found=False, nodes={}):
        self.found = found
        self.nodes = nodes

    def addWord(self, word):
        if word == "":
            self.found = True
        else:
            c = word[0]
            if c not in self.nodes:
                self.nodes[c] = Node(nodes={})
            nextNode = self.nodes[c]
            return nextNode.addWord(word[1:])

    def findWord(self, word, start_idx) -> List[int]:
        n = len(word)
        node = self
        found_idx = []
        for i in range(start_idx, n + 1):
            if node.found:
                found_idx.append(i)

            if i < n and word[i] in node.nodes:
                node = node.nodes[word[i]]
            else:
                break

        return found_idx


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        n = len(s)
        root = Node(nodes={})
        for word in wordDict:
            root.addWord(word)

        ans = []
        q = [(0, ())]
        while q:
            i, prev_comb = q.pop()
            if i == n:
                combined_string = s[:prev_comb[0]]
                for j in range(1, len(prev_comb)):
                    combined_string += " " + s[prev_comb[j - 1]: prev_comb[j]]
                ans.append(combined_string)

            for next_idx in root.findWord(s, i):
                q.append((next_idx, prev_comb + (next_idx,)))

        return ans
