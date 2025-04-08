class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        counter = Counter(nums)
        counter2 = Counter(counter.values())

        if len(counter2) == 0 or (len(counter2) == 1 and list(counter2.keys())[0] == 1):
            return 0

        n = len(nums)
        count = 0
        i = 0
        while i < n:
            for j in range(min(3, n - i)):
                num = nums[i + j]
                prev_count = counter[num]
                counter[num] -= 1
                counter2[prev_count] -= 1
                if counter2[prev_count] == 0:
                    del counter2[prev_count]
                if counter[num] > 0:
                    counter2[counter[num]] += 1
            i += 3
            count += 1

            # print(counter2)

            if len(counter2) == 0 or (len(counter2) == 1 and list(counter2.keys())[0] == 1):
                return count

        return count