class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        s_low, s_high = str(low), str(high)
        n_low, n_high = len(s_low), len(s_high)
        s_low = '0' * (n_high - n_low) + s_low

        def generate(count, missing):
            nonlocal s_low, s_high
            prefix = '0' * missing
            if count >= 10:
                return []
            arr = []
            for i in range(1, 11 - count):
                s = prefix + ''.join([str(x) for x in range(i, count + i)])
                if s_low <= s <= s_high:
                    arr.append(int(s))
            return arr

        ans = []
        for i in range(n_low, n_high + 1):
            if i >= 10:
                break
            ans += generate(i, n_high - i)
        return ans
