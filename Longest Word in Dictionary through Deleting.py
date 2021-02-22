class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        pt = {word: 0 for word in d}
        max_len = 0
        longest = []
        for c in s:
            to_delete = []
            for word, idx in pt.items():
                if word[idx] == c:
                    idx += 1
                    pt[word] = idx
                    if idx == len(word):
                        to_delete.append(word)
                        if idx > max_len:
                            longest = [word]
                            max_len = idx
                        elif idx == max_len:
                            longest.append(word)
            for deleting in to_delete:
                del pt[deleting]
        return sorted(longest)[0] if max_len else ''


# Time: O(nd) for n length of s and m length of word in d and d being size of array/list
# Space: O(d)

# Runtime: 312 ms, faster than 71.51% of Python3 online submissions for Longest Word in Dictionary through Deleting.
# Memory Usage: 16.8 MB, less than 66.00% of Python3 online submissions for Longest Word in Dictionary through Deleting.

class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        trie = {}
        for word in d:
            dp = trie
            for i, c in enumerate(word):
                last_char = i == len(word)-1
                if c not in dp:
                    dp[c] = (last_char, word if last_char else '', {})
                if i != len(word) - 1:
                    dp = dp[c][2]

        explored = [trie]
        longest = []
        max_len = 0
        for c in s:
            new_explored = []
            for node in explored:
                if c in node:
                    if node[c][0]:
                        if len(node[c][1]) > max_len:
                            longest = [node[c][1]]
                            max_len = len(node[c][1])
                        elif len(node[c][1]) == max_len:
                            longest.append(node[c][1])
                    new_explored.append(node[c][2])
            explored += new_explored
        return sorted(longest)[0] if max_len else ''
        