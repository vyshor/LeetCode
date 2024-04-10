class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n = len(deck)
        deck.sort()
        i = n-2
        q = deque([deck[-1]])
        while i >= 0:
            q.appendleft(q.pop())
            q.appendleft(deck[i])
            i -= 1
        return q
