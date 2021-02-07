from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        q = deque([(beginWord, 1)])
        while len(q) > 0:
            word, path = q.popleft()
            for idx, l in enumerate(word):
                for c in 'abcdefghijklmnopqrstuvwyxz':
                    new_word = word[:idx] + c + word[idx+1:]
                    if new_word in wordList:
                        if new_word == endWord:
                            return path + 1
                        wordList.remove(new_word)
                        q.append((new_word, path+1))
        return 0


# Runtime: 444 ms, faster than 40.25% of Python3 online submissions for Word Ladder.
# Memory Usage: 15.2 MB, less than 79.39% of Python3 online submissions for Word Ladder.

# Time: O(nm) for n being the length of the wordList, and m being the length of each word
# Space: O(nm)


import heapq

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def oneLetterDiffer(a, b):
            differCount = 0
            for idx, a1 in enumerate(a):
                if a1 != b[idx]:
                    differCount += 1
                    if differCount > 1:
                        return False
            return True

        dp = {}
        dp2 = {}
        dp3 = {}

        for word in wordList:
            dp2[word] = True

            differCount = 0
            for idx, a1 in enumerate(word):
                if a1 != endWord[idx]:
                    differCount += 1
            dp3[word] = differCount

        if not dp2.get(endWord):
            return 0

        wordList.append(beginWord)

        # Construct graph
        for word in wordList:
            new_connections = []
            for exist_word in dp.keys():
                if oneLetterDiffer(exist_word, word):
                    new_connections.append(exist_word)
                    dp[exist_word].append(word)
            dp[word] = new_connections


        # BFS


        visited = {beginWord: True}
        q = []
        for word in dp.get(beginWord):
            heapq.heappush(q, (2 + dp3[word], 2, word))

        while len(q) > 0:
            _, path_len, word = heapq.heappop(q)

            visited[word] = True
            if word == endWord:
                return path_len
            for next_word in dp.get(word):
                if not visited.get(next_word):
                    heapq.heappush(q, (path_len + 1 + dp3[word], path_len + 1, next_word))
        return 0