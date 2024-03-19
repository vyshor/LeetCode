class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        maxx = len(tasks)
        counter = Counter(tasks)
        arr = [(-count, val) for val, count in counter.items()]
        heapq.heapify(arr)

        count, _ = heapq.heappop(arr)
        first_count = -count
        first_max = n*(first_count-1)+first_count
        maxx = max(maxx, first_max)
        while arr and arr[0][0] == -first_count:
            heapq.heappop(arr)
            first_max += 1
            maxx = max(maxx, first_max)

        return maxx
