class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        _, prefix = min([(len(x), x) for x in strs])
        for s in strs:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if prefix == "":
                    return prefix
        return prefix

# Runtime 33 ms Beats 75.95%
# Memory 13.9 MB Beats 77.26%