class Solution:
    def minimumPushes(self, word: str) -> int:
        counter = Counter(list(word))
        q = [-val for val in counter.values()]
        q.sort()
        pushes = 0
        num_pad = 0
        rotation = 1
        for count in q:
            pushes += -count * rotation
            num_pad += 1
            if num_pad == 8:
                rotation += 1
                num_pad = 0
        return pushes
