class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        counter = Counter(answers)
        total = 0
        for num, count in counter.items():
            total += math.ceil(count / (num + 1)) * (num + 1)
        return total
