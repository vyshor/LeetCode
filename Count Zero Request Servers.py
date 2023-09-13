class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        n_log = len(logs)
        times = [(t, server_id) for (server_id, t) in logs]
        times.sort()

        m = len(queries)
        ans = [n] * m
        q = [(query, i) for i, query in enumerate(queries)]
        q.sort()

        left, right = 0, 0
        counter = {}
        for query in q:
            t, i = query
            while right < n_log and times[right][0] <= t:
                if times[right][1] not in counter:
                    counter[times[right][1]] = 1
                else:
                    counter[times[right][1]] += 1
                right += 1

            while left < n_log and times[left][0] < t - x:
                counter[times[left][1]] -= 1
                if counter[times[left][1]] == 0:
                    del counter[times[left][1]]
                left += 1

            ans[i] -= len(counter)

        return ans


