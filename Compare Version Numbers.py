class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = [int(i) for i in version1.split(".")]
        v2 = [int(i) for i in version2.split(".")]
        n = max(len(v1), len(v2))
        while len(v1) < n:
            v1.append(0)
        while len(v2) < n:
            v2.append(0)

        if v1 < v2:
            return -1
        elif v2 < v1:
            return 1
        return 0

# class Solution:
#     def compareVersion(self, version1: str, version2: str) -> int:
#         v1, v2 = [int(i) for i in version1.split(".")], [int(i) for i in version2.split(".")]
#
#         def compare(a, b):
#             na, nb = len(a), len(b)
#             n = max(na, nb)
#             while len(a) < n:
#                 a.append(0)
#
#             while len(b) < n:
#                 b.append(0)
#
#             for i in range(n):
#                 if a[i] < b[i]:
#                     return -1
#                 elif a[i] > b[i]:
#                     return 1
#             return 0
#
#         return compare(v1, v2)
