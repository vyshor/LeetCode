class Solution:
    def countAnagrams(self, s: str) -> int:
        MOD = 10 ** 9 + 7
        count = 1
        words = s.split(' ')
        for word in words:
            n = len(word)
            counter = Counter(word)
            count *= math.factorial(n)
            for freq in counter.values():
                count //= math.factorial(freq)
            count %= MOD
        return count
