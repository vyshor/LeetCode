class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = {}
        idx = 0
        unexplored = [(idx, 1)]
        while unexplored:
            idx, upp = unexplored.pop()
            for idx2 in range(upp - 1, idx - 1, -1):
                if not dp.get(idx2):
                    num = nums[idx2]
                    dp[idx2] = True
                    if idx2 + num >= len(nums) - 1:
                        return True
                    else:
                        if not dp.get(idx2 + num):
                            unexplored += [(idx2, idx2 + num + 1)]
        return False

# Runtime: 112 ms, faster than 17.28% of Python3 online submissions for Jump Game.
# Memory Usage: 18.1 MB, less than 7.14% of Python3 online submissions for Jump Game.

# Time: O(n)
# Space: O(n)

"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]

"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
["aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa","ba"]