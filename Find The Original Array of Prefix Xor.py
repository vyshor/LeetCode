class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        n = len(pref)
        ans = [pref[0]]
        for i in range(1, n):
            ans.append(pref[i-1] ^ pref[i])
        return ans
