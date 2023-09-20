class Solution:
    def numWays(self, s: str) -> int:
        counter = Counter(s)
        three_split = counter["1"] // 3

        if counter["1"] % 3 != 0:
            return 0

        if counter["1"] == 0:
            return ((counter["0"] - 1) * (counter["0"] - 2) // 2) % (10 ** 9 + 7)

        count = three_split
        splitA = 0
        stopA = False
        splitB = 0
        stopB = True

        for i, c in enumerate(s):
            if c == "1":
                if not stopA and splitA > 0:
                    stopA = True
                    stopB = False
                    count = three_split
                if not stopB and splitB > 0:
                    break
                count -= 1

            if not stopA and count <= 0:
                splitA += 1

            if not stopB and count <= 0:
                splitB += 1

        # print(splitA, splitB)
        return ((splitA % (10 ** 9 + 7)) * (splitB % (10 ** 9 + 7))) % (10 ** 9 + 7)
