class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        nums = []
        count = {}
        num_len = {}
        pos = {}
        total_num = 0
        total_cost = 0
        for new_num in instructions:
            # if type(count.get(new_num)) != int:
            if new_num not in count.keys():
                for idx, num in enumerate(nums):
                    if num > new_num:
                        insert_position = idx
                        total_cost += min(count[num], total_num - count[num])
                        count[new_num] = count[num]
                        num_len[new_num] = 1
                        break

                    if idx == len(nums) - 1:
                        insert_position = idx+1
                        count[new_num] = count[num] + num_len[num]
                        num_len[new_num] = 1

                if len(nums) == 0:
                    insert_position = 0
                    count[new_num] = 0
                    num_len[new_num] = 1

                nums.insert(insert_position, new_num)
                pos[new_num] = insert_position
                for i in range(insert_position+1,len(nums)):
                    count[nums[i]] += 1
                    pos[nums[i]] += 1
            else:
                total_cost += min(count[new_num], total_num - count[new_num] - num_len[new_num])
                num_len[new_num] += 1
                for i in range(pos[new_num]+1,len(nums)):
                    count[nums[i]] += 1
            # print(nums)
            # print(count)
            # print(total_cost)
            total_num += 1
        return total_cost

from sortedcontainers import SortedList

class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        ll = SortedList()
        total_cost = 0
        for num in instructions:
            total_cost += min(ll.bisect_left(num), len(ll) - ll.bisect_right(num))
            total_cost %= 10 ** 9 + 7
            ll.add(num)
        return total_cost

# Runtime: 6144 ms, faster than 40.24% of Python3 online submissions for Create Sorted Array through Instructions.
# Memory Usage: 29.6 MB, less than 29.76% of Python3 online submissions for Create Sorted Array through Instructions.

# Time: O(nlgn) for n being number of numbers in instruction
# Space: O(n)