class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        negative_shift = -100
        uses = [0] * n
        available = list(range(n))
        q = deque([])
        heapq.heapify(meetings)
        while meetings:
            start, end = heapq.heappop(meetings)
            if end > 0: # Indicating start of meeting
                q.append((start, end))
            else:
                heapq.heappush(available, end-negative_shift)

            while available and q:
                waiting_start, waiting_end = q.popleft()
                duration = waiting_end - waiting_start
                room = heapq.heappop(available)
                uses[room] += 1
                heapq.heappush(meetings, [start+duration, negative_shift+room])

        maxx_count = uses[0]
        j = 0
        for i, use in enumerate(uses):
            if use > maxx_count:
                j = i
                maxx_count = use
        return j
