class Solution:
    def simplifyPath(self, path: str) -> str:
        ll = path.split('/')
        conpath = []
        for f in ll:
            if f == '' or f == '.':
                continue
            if f == '..':
                if conpath:
                    conpath.pop()
                continue
            conpath.append(f)
        return '/'  + '/'.join(conpath)

# Runtime: 28 ms, faster than 89.96% of Python3 online submissions for Simplify Path.
# Memory Usage: 14.4 MB, less than 49.67% of Python3 online submissions for Simplify Path.

# Time: O(n)
# Space: O(n)
