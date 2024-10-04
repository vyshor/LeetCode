class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        if n % 2 == 1:
            return -1

        skill.sort()
        avg = skill[0] + skill[-1]
        i, j = 0, len(skill)-1
        chemistry = 0
        while i < j:
            if skill[i] + skill[j] != avg:
                return -1
            chemistry += skill[i] * skill[j]
            i += 1
            j -= 1
        return chemistry
