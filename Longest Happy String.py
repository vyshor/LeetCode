class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        q = []
        if a:
            q.append((-a, 'a'))
        if b:
            q.append((-b, 'b'))
        if c:
            q.append((-c, 'c'))

        prev = ''
        ans = ''
        heapq.heapify(q)
        while q:
            count, letter = heapq.heappop(q)
            if letter == prev:
                if not q:
                    return ans
                else:
                    count2, letter2 = heapq.heappop(q)
                    count2 += 1
                    ans += letter2
                    if count2:
                        heapq.heappush(q, (count2, letter2))

            used = min(-count, 2)
            count += used
            ans += letter * used
            if count:
                heapq.heappush(q, (count, letter))
            prev = letter
        return ans
