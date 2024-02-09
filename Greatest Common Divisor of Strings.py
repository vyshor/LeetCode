class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""

        def gcd(a, b):
            if a < b:
                a, b = b, a

            while b != 0:
                a, b = b, a % b
            return a

        return str1[:gcd(len(str1), len(str2))]


