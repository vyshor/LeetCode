class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        ans = ['']
        for c in S:
            if c.isalpha():
                new_ans = []
                for word in ans:
                    new_ans.append(word +  c.lower())
                    new_ans.append(word +  c.upper())
                ans = new_ans
            else:
                ans = [a + c for a in ans]
        return ans

# Time: O(2^n)
# Space: O(2^n)

# Runtime: 44 ms, faster than 98.57% of Python3 online submissions for Letter Case Permutation.
# Memory Usage: 14.7 MB, less than 92.31% of Python3 online submissions for Letter Case Permutation.
