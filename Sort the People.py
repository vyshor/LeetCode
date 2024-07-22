class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(names)
        arr = sorted([(heights[i], names[i]) for i in range(n)], reverse=True)
        return [n for (_, n) in arr]

