class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        ans = min(citations[0], 1)
        start, end = 0, n
        while start < end:
            mid = (start + end) // 2
            # print(start, end, mid)
            if citations[mid] >= n - mid:
                ans = max(ans, n - mid)

                end = mid
            else:
                if start == end - 1:
                    break

                start = mid
        return ans
