class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Complement is calculated and try to find in remaining
        # Num is added to every number in dp
        # And complement of the two numbers is added into remaining
        dp = []
        remaining = {}
        ans = {}
        for num in nums:
            try:
                remaining[num]
                for valid_ans in remaining[num]:
                    valid_ans_lst = sorted(valid_ans + [num])
                    ans[str(valid_ans_lst)] = valid_ans_lst
            except KeyError:
                pass
            for x_num in dp:
                remainder = -1 * (x_num + num)
                try:
                    remaining[remainder]
                    remaining[remainder].append([x_num, num])
                except KeyError:
                    remaining[remainder] = [[x_num, num]]
            dp.append(num)

        return ans.values()

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = {}
        nums.sort()
        n = len(nums)
        for idx, num in enumerate(nums):
            if idx >= n - 2:
                break
            front = idx + 1
            back = n - 1
            while front < back:
                if num + nums[front] + nums[back] == 0:
                    valid_ans_lst = [num, nums[front], nums[back]]
                    ans[str(valid_ans_lst)] = valid_ans_lst
                    front += 1
                    back -= 1
                elif num + nums[front] + nums[back] < 0:
                    front += 1
                else:
                    back -= 1
        return ans.values()

# Time: O(n^2)
# Space: O(1)
# Runtime: 2620 ms, faster than 5.02% of Python3 online submissions for 3Sum.
# Memory Usage: 18.7 MB, less lessthan 5.71% of Python3 online submissions for 3Sum.
