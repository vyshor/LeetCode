class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        count =  0
        for ch in s:
            if c == ch:
                count += 1
        return count * (count+1) // 2
