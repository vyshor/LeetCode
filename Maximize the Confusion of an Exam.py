class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        n = len(answerKey)
        ans = 0

        for target in ['T', 'F']:
            left, right = 0, 0
            replacements = 0
            while right < n:
                if answerKey[right] == target:
                    ans = max(ans, right - left + 1)
                    right += 1
                else:
                    replacements += 1
                    while replacements > k:
                        if answerKey[left] != target:
                            replacements -= 1
                        left += 1
                    ans = max(ans, right - left + 1)
                    right += 1

        return ans
