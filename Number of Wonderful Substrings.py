class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        counter = {0: 1}
        current = 0
        count = 0
        for c in word:
            shift = 1<<(ord(c)-97)
            current ^= shift

            if current in counter:
                count += counter[current]
                counter[current] += 1
            else:
                counter[current] = 1

            for i in range(10):
                poss_mask = current ^ (1<<i)
                if poss_mask in counter:
                    count += counter[poss_mask]
        return count
