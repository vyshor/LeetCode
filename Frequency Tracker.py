class FrequencyTracker:

    def __init__(self):
        self.dp = {}
        self.count = {}

    def add(self, number: int) -> None:
        if number not in self.dp:
            self.dp[number] = 1
        else:
            self.dp[number] += 1

        count = self.dp[number]
        if count not in self.count:
            self.count[count] = {number}
        else:
            self.count[count].add(number)

        if count - 1 != 0:
            self.count[count - 1].remove(number)
            if len(self.count[count - 1]) == 0:
                del self.count[count - 1]

    def deleteOne(self, number: int) -> None:
        if number not in self.dp:
            return

        self.dp[number] -= 1
        count = self.dp[number]
        if count == 0:
            del self.dp[number]
        else:
            if count not in self.count:
                self.count[count] = {number}
            else:
                self.count[count].add(number)

        self.count[count + 1].remove(number)
        if len(self.count[count + 1]) == 0:
            del self.count[count + 1]

    def hasFrequency(self, frequency: int) -> bool:
        return frequency in self.count

# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)
