class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counter = {}
        for s in strs:
            arr = [0] * 26
            for c in s:
                arr[ord(c)-97] += 1
            key = str(arr)
            if key not in counter:
                counter[key] = [s]
            else:
                counter[key].append(s)
        return list(counter.values())

# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         strs2 = [''.join(sorted(word)) for word in strs]
#         ans = {}
#         for id, u_str in enumerate(strs2):
#             try:
#                 ans[u_str]
#                 ans[u_str].append(strs[id])
#             except KeyError:
#                 ans[u_str] = [strs[id]]
#         ans = reversed(list(ans.values()))
#         return ans
#
# # Time: O(nxlgx) for n words, and x max characters for each word
# # Space: O(nx)
# # Runtime: 108 ms, faster than 91.50% of Python3 online submissions for Group Anagrams.
# # Memory Usage: 16.5 MB, less than 45.28% of Python3 online submissions for Group Anagrams.
