class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        n = len(bank)
        counter = Counter(bank[0])
        prev = counter.get("1", 0)
        count = 0
        for i in range(1, n):
            counter = Counter(bank[i])
            current = counter.get("1", 0)
            if current != 0:
                count += prev * current
                prev = current
        return count
