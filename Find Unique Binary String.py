class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        i = 0
        s = ""
        for num in nums:
            if num[i] == "0":
                s += "1"
            else:
                s += "0"
            i += 1
        return s
