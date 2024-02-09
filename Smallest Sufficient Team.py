class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        n = len(people)
        m = len(req_skills)
        mapping = {}
        dp = {0: 0}
        dp_team = {0: ()}

        for i, skill in enumerate(req_skills):
            mapping[skill] = i

        for i, skills in enumerate(people):
            skillset = 0
            for skill in skills:
                skillset |= 1 << mapping[skill]

            for prev_state in list(dp.keys()):
                count = dp[prev_state]
                team = dp_team[prev_state]
                new_state = prev_state | skillset
                if new_state in dp:
                    if count + 1 < dp[new_state]:
                        dp[new_state] = count + 1
                        dp_team[new_state] = team + (i,)
                else:
                    dp[new_state] = count + 1
                    dp_team[new_state] = team + (i,)

        return dp_team[(1 << m) - 1]
