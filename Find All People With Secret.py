class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        known = {0, firstPerson}
        meetings.sort(key=lambda meeting: meeting[2])

        prev_t = 0
        dp = {}
        for (x, y, t) in meetings:
            if t != prev_t:
                dp = {}
                prev_t = t

            # In the case where both do not know secret
            if x not in known and y not in known:
                if x not in dp:
                    dp[x] = {y}
                else:
                    dp[x].add(y)

                if y not in dp:
                    dp[y] = {x}
                else:
                    dp[y].add(x)
            else:  # At least one know secret
                q = [x, y]
                while q:
                    person = q.pop()

                    known.add(person)
                    if person in dp:
                        for other_person in dp[person]:
                            if other_person in dp:
                                q.append(other_person)
                        del dp[person]

        return known
