class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        m = len(requests)
        total_requests = 0
        states = [0] * n
        ans = 0

        def exploreRequest(i):
            nonlocal ans, total_requests, states
            if i == m:
                if not any(states):
                    ans = max(ans, total_requests)
                return

            fro, to = requests[i]
            states[fro] -= 1
            states[to] += 1
            total_requests += 1

            exploreRequest(i + 1)

            states[fro] += 1
            states[to] -= 1
            total_requests -= 1

            exploreRequest(i + 1)

        exploreRequest(0)

        return ans
