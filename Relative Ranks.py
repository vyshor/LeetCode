class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        arr = sorted(score, reverse=True)
        scores = {}
        names = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        for i, num in enumerate(arr):
            if i < 3:
                scores[num] = names[i]
            else:
                scores[num] = str(i + 1)

        for i in range(len(arr)):
            score[i] = scores[score[i]]
        return score
