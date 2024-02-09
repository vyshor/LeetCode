class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        even, odd = {}, {}

        for i in range(n1):
            c = s1[i]
            if i % 2 == 0:
                if c not in even:
                    even[c] = 1
                else:
                    even[c] += 1
            else:
                if c not in odd:
                    odd[c] = 1
                else:
                    odd[c] += 1

        for i in range(n2):
            c = s2[i]
            if i % 2 == 0:
                if c not in even:
                    return False
                else:
                    even[c] -= 1
                    if even[c] < 0:
                        return False
            else:
                if c not in odd:
                    return False
                else:
                    odd[c] -= 1
                    if odd[c] < 0:
                        return False

        return True



