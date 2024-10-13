class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        n = 0
        q = []
        chairs = []
        times = [(arrival, leaving, i) for i, (arrival, leaving) in enumerate(times)]
        times.sort()

        # print(times)

        for arrival, leaving, i in times:
            while chairs and chairs[0][0] <= arrival:
                _, seat = heapq.heappop(chairs)
                heapq.heappush(q, seat)

            seat_num = n
            if q:
                seat_num = heapq.heappop(q)
            else:
                n += 1

            # print(arrival, chairs, n)
            if i == targetFriend:
                return seat_num

            heapq.heappush(chairs, (leaving, seat_num))
