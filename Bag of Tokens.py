class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        if not tokens:
            return 0

        tokens.sort()
        n = len(tokens)
        summ = 0
        prefix = []
        maxx = 0

        if power < tokens[0]:
            return 0

        for i, token in enumerate(tokens):
            summ += token
            prefix.append(summ)
            if power >= summ:
                maxx = max(maxx, i + 1)

        for i, prefix_sum in enumerate(prefix):
            total_power = summ - prefix_sum + power
            if total_power >= prefix_sum:
                maxx = max(maxx, (i + 1) - (n - (i + 1)))

            excess_power = total_power - prefix_sum
            if i + 1 < n and tokens[i + 1] <= excess_power:
                maxx = max(maxx, (i + 1) - (n - (i + 1)) + 1)

        return maxx
