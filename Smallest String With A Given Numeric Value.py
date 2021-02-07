class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        d = 'abcdefghijklmnopqrstuvwxyz'
        ans = ''
        k -= n
        num_val_max = k // 25
        ans += 'z' * num_val_max
        k -= num_val_max * 25
        if k:
            ans += d[(k % 26)]
        ans += 'a' * (n - len(ans))
        return ans[::-1]



# Runtime: 60 ms, faster than 80.67% of Python3 online submissions for Smallest String With A Given Numeric Value.
# Memory Usage: 15.2 MB, less than 91.64% of Python3 online submissions for Smallest String With A Given Numeric Value.

# Time: O(1)
# Space: O(n)