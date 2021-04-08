class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        m = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        dp = set(m[digits[0]])
        for idx, d in enumerate(digits):
            if idx != 0:
                for old_comb in list(dp):
                    dp.remove(old_comb)
                    for c in m[d]:
                        dp.add(old_comb + c)
        return list(dp)

# Runtime: 32 ms, faster than 54.65% of Python3 online submissions for Letter Combinations of a Phone Number.
# Memory Usage: 14.2 MB, less than 64.02% of Python3 online submissions for Letter Combinations of a Phone Number.

# Time: O(4^n * n)
# Space: O(n)
