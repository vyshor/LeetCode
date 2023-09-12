class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 1:
            return nums

        count1, count2 = 0, 0
        num1, num2 = 0, 1

        for num in nums:
            if num == num1:
                count1 += 1
            elif num == num2:
                count2 += 1
            elif count1 == 0:
                num1 = num
                count1 = 1
            elif count2 == 0:
                num2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1

        count1, count2 = 0, 0
        for num in nums:
            if num == num1:
                count1 += 1
            elif num == num2:
                count2 += 1

        ans = []
        # print(num1, num2)
        # print(count1, count2, n // 3)
        if count1 > n // 3:
            ans.append(num1)

        if num2 != num1:
            if count2 > n // 3:
                ans.append(num2)
        return ans
