class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        stack = []
        curr = ""
        max_len = 0

        for c in s:
            # print(c, stack)
            if c.isdigit():
                factor = int(c)
                prev_len = max_len
                before_len = prev_len - len(curr)
                max_len *= factor
                stack.append((curr, before_len, prev_len))
                curr = ""

                if max_len >= k:
                    # print(stack)
                    while stack:
                        curr, before_len, prev_len = stack.pop()
                        k = ((k-1) % prev_len)+1
                        if k > before_len:
                            return curr[k - before_len - 1]

            else:
                curr += c
                max_len += 1

                if max_len == k:
                    return c
