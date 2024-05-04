class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        count = 0
        i, j = 0, len(people) -1
        while i <= j:
            other = limit - people[i]
            while i < j and people[j] > other:
                j -= 1
                count += 1

            if i < j and people[j] <= limit:
                j -= 1

            count += 1
            i += 1

        return count


# class Solution:
#     def numRescueBoats(self, people: List[int], limit: int) -> int:
#         people.sort(reverse=True)
#         boats = 0
#         p1 = 0
#         p2 = len(people) - 1
#         while p1 < p2:
#             excess = limit - people[p1]
#             if people[p2] <= excess:
#                 p2 -= 1
#             p1 += 1
#             boats += 1
#
#         if p1 == p2:
#             boats += 1
#         return boats
#
# # Runtime: 444 ms, faster than 81.09% of Python3 online submissions for Boats to Save People.
# # Memory Usage: 21.1 MB, less than 49.42% of Python3 online submissions for Boats to Save People.
#
# # Time: O(nlgn + n), nlgn for the timsort, n for the iteration
# # Space: O(1)
