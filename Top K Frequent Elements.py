class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dp = {}
        for num in nums:
            if dp.get(num):
                dp[num] += 1
            else:
                dp[num] = 1

        most_freq = []
        for x in range(k):
            max_freq = 0
            max_value = ''
            for key, value in dp.items():
                if value > max_freq:
                    max_value = key
                    max_freq = value
            if max_freq:
                most_freq.append(max_value)
                del dp[max_value]
        return most_freq if most_freq else None

# Time: O(n*k)
# Space: O(n*k)
# Runtime: 212 ms, faster than 5.10% of Python3 online submissions for Top K Frequent Elements.
# Memory Usage: 18.1 MB, less than 6.25% of Python3 online submissions for Top K Frequent Elements.