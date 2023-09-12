class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        req = [0] * numCourses
        dp = {}
        ans = []
        count = 0

        for prereq in prerequisites:
            a, b = prereq
            req[a] += 1

            if b not in dp:
                dp[b] = [a]
            else:
                dp[b].append(a)

        q = []
        for i in range(numCourses):
            if req[i] == 0:
                q.append(i)

        while q:
            i = q.pop()

            ans.append(i)
            if i in dp:
                for course in dp[i]:
                    req[course] -= 1
                    if req[course] == 0:
                        q.append(course)

        if len(ans) < numCourses:
            return []

        return ans

