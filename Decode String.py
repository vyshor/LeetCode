class Solution:
    def decodeString(self, s: str) -> str:
        stack = list(s)
        stack2 = []
        while stack:
            c = stack.pop()
            if c == "[":
                new_s = ""
                while True:
                    c2 = stack2.pop()
                    if c2 != "]":
                        new_s += c2
                    else:
                        break

                count = stack.pop()
                while stack and stack[-1].isdigit():
                    count = stack.pop() + count
                else:
                    stack.append(new_s * int(count))
            else:
                stack2.append(c)

        return "".join(stack2[::-1])
