class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        counter = Counter(secret)
        bulls = 0
        cows = 0
        for i, num in enumerate(guess):
            if num == secret[i]:
                bulls += 1
                counter[num] -= 1
                if counter[num] < 0:
                    cows -= 1
                    counter[num] += 1
            else:
                if num in counter and counter[num] > 0:
                    cows += 1
                    counter[num] -= 1

        return str(bulls) + "A" + str(cows) + "B"
