import math as m
class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        if not bound:
            return []
        ans = set([])
        if x > 1:
            _x = [x**i for i in range(int(m.log(bound, x))+1)]
        else:
            _x = [1]
        if y > 1:
            _y = [y**i for i in range(int(m.log(bound, y))+1)]
        else:
            _y = [1]
        for x_val in _x:
            for y_val in _y:
                total = x_val + y_val
                if total <= bound:
                    if total not in ans:
                        ans.add(total)
                else:
                    break
        return list(ans)

# Runtime: 32 ms, faster than 69.17% of Python3 online submissions for Powerful Integers.
# Memory Usage: 14.4 MB, less than 30.42% of Python3 online submissions for Powerful Integers.

# Time: O(logx bound * logy bound)
# Space: O(logx bound * logy bound)

