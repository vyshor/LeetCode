class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda p: (-p[0], p[1]))
        ans = []
        for p in people:
            ans.insert(p[1], p)
        return ans

# class Solution:
#     def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
#         n = len(people)
#         choices = [(person[1], person[0], person[1]) for person in people]
#         heapq.heapify(choices)
#         q = []
#
#         while choices:
#             _, h, k = choices[0]
#             m = len(choices)
#             q.append((h, k))
#
#             if len(q) == n:
#                 return q
#
#             new_choices = []
#             for i in range(1, m):
#                 remaining, old_h, old_k = choices[i]
#                 if h >= old_h:
#                     remaining -= 1
#                 new_choices.append((remaining, old_h, old_k))
#             heapq.heapify(new_choices)
#             choices = new_choices
