# class Solution:
#     def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
#         preq_lst = [[] for x in
#                     range(numCourses)]  # lst[1] means all the courses needed to be completed before 1 can be completed
#         preq_lst2 = [[] for x in range(numCourses)]  # lst[1] means all the courses that have 1 has pre-requisite
#         preq_state = [0] * numCourses
#
#         def explore(i):
#             if preq_state[i]:
#                 return
#             else:
#                 if all([preq_state[x] for x in preq_lst[i]]):
#                     preq_state[i] = 1
#                     for other_state in preq_lst2[i]:
#                         # print(other_state)
#                         explore(other_state)
#
#         for preq in prerequisites:
#             preq_lst[preq[0]].append(preq[1])
#             preq_lst2[preq[1]].append(preq[0])
#
#         # print(preq_lst)
#
#         for i in range(numCourses):
#             if not preq_lst[i]:
#                 explore(i)
#             # print(preq_state)
#
#         # print(preq_state)
#         return all(preq_state)

# Time: O(n*k+k) = O(n*k),  k for the number
# Space: O(n)
# Runtime: 120 ms, faster than 41.89% of Python3 online submissions for Course Schedule.
# Memory Usage: 17.5 MB, less than 6.12% of Python3 online submissions for Course Schedule.

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edges = {}
        indegrees = [0] * numCourses

        for (next, prev) in prerequisites:
            indegrees[next] += 1
            if prev not in edges:
                edges[prev] = set()
            edges[prev].add(next)

        q = []
        for i in range(numCourses):
            if indegrees[i] == 0:
                q.append(i)

        count = 0
        while q:
            i = q.pop()
            count += 1
            if i in edges:
                for j in edges[i]:
                    indegrees[j] -= 1
                    if indegrees[j] == 0:
                        q.append(j)

        return count == numCourses
