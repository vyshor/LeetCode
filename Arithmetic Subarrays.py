class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def check(left, right):
            if left >= right-1:
                return True

            arr = nums[left:right+1]
            heapq.heapify(arr)
            first, second = heapq.heappop(arr), heapq.heappop(arr)
            diff = second - first
            first = second
            while arr:
                second = heapq.heappop(arr)
                if second - first != diff:
                    return False

                first = second
            return True

        n = len(l)
        ans = []
        for i in range(n):
            ans.append(check(l[i], r[i]))
        return ans
