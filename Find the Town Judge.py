class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        people = set(range(1, n+1))
        trusted = {}
        for (person, target) in trust:
            if person in people:
                people.remove(person)

            if target not in trusted:
                trusted[target] = {person}
            else:
                trusted[target].add(person)

        if len(people) > 1 or len(people) == 0:
            return -1

        judge = list(people)[0]

        if judge == 1 and n == 1:
            return judge

        return judge if judge in trusted and len(trusted[judge]) == n-1 else -1
