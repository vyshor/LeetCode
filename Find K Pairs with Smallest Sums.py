class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        n1 = len(nums1)
        n2 = len(nums2)

        q = [(0, (0, 0))]
        count = 0
        ans = []
        visited = set()

        while count < k and q:
            _, (i, j) = heapq.heappop(q)

            if (i, j) in visited:
                continue

            visited.add((i, j))
            ans.append([nums1[i], nums2[j]])
            count += 1

            for (x, y) in [(i + 1, j), (i, j + 1)]:
                if x < n1 and y < n2 and (x, y) not in visited:
                    heapq.heappush(q, (nums1[x] + nums2[y], (x, y)))

        return ans
