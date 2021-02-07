class Solution:
    def nextGreaterElement(self, n: int) -> int:
        ll = [int(i) for i in list(str(n))]
        prev_digit =  ll[-1]
        for idx in range(len(ll)-1, -1, -1):
            if ll[idx] < prev_digit:
                current_idx = idx
                current_num = ll[idx]
                while idx+1 < len(ll) and ll[idx+1] > current_num:
                    idx += 1
                ll[current_idx], ll[idx] = ll[idx], ll[current_idx]
                ll[current_idx+1:] = reversed(ll[current_idx+1:])
                ans = int(''.join([str(i) for i in ll]))
                return ans if ans < 2 **31 else -1
            prev_digit = ll[idx]
        return -1

# Runtime: 36 ms, faster than 11.03% of Python3 online submissions for Next Greater Element III.
# Memory Usage: 14.4 MB, less than 27.07% of Python3 online submissions for Next Greater Element III.

# Time: O(n)
# Space: O(1)