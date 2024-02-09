class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        else:
            s = "1"
            prev = ""
            count = 0
            for _ in range(2, n + 1):
                new_s = ""
                for c in s:
                    if c != prev:
                        if prev != "":
                            new_s += str(count) + prev

                        prev = c
                        count = 1
                    else:
                        count += 1

                if prev != "":
                    new_s += str(count) + prev

                s = new_s
                prev = ""
                count = 0

            return s

