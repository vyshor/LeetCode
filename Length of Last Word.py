class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        have_space = True
        for c in s:
            if c == " ":
                have_space = True
            elif have_space:
                count = 1
                have_space = False
            else:
                count += 1
        return count

# class Solution:
#     def lengthOfLastWord(self, s: str) -> int:
#         return len(s.strip().split(" ")[-1])
