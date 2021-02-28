class FreqStack:

    def __init__(self):
        self.stack = {}
        self.counter = {}
        self.most_freq_count = 0

    def push(self, x: int) -> None:
        if x not in self.counter:
            self.counter[x] = 1
            count = 1
        else:
            self.counter[x] += 1
            count = self.counter[x]
        if count not in self.stack:
            self.stack[count] = [x]
        else:
            self.stack[count].append(x)
        self.most_freq_count = max(count, self.most_freq_count)

    def pop(self) -> int:
        ans = self.stack[self.most_freq_count].pop()
        self.counter[ans] -= 1
        if not self.stack[self.most_freq_count]:
            self.most_freq_count -= 1
        return ans


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()

# Time:
#     Push: O(1)
#     Pop: O(1)
# Space: O(n)

# Runtime: 304 ms, faster than 80.11% of Python3 online submissions for Maximum Frequency Stack.
# Memory Usage: 22.4 MB, less than 43.37% of Python3 online submissions for Maximum Frequency Stack.


class FreqStack:

    def __init__(self):
        self.stack = []
        self.counter = {}

    def push(self, x: int) -> None:
        if x not in self.counter:
            self.counter[x] = 1
        else:
            self.counter[x] += 1
        self.stack.append(x)

    def pop(self) -> int:
        s = len(self.stack) - 1
        most_freq_count = max(list(self.counter.values()))
        for i in range(s, -1, -1):
            if i == len(self.stack) - 1 and self.stack[i] == 'X':
                self.stack.pop()
            elif self.stack[i] == 'X':
                continue
            elif self.counter[self.stack[i]] == most_freq_count:
                ans, self.stack[i] = self.stack[i], 'X'
                self.counter[ans] -= 1
                if self.counter[ans] == 0:
                    del self.counter[ans]
                return ans

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()

# Time:
#     Push: O(1)
#     Pop: O(n)
# Space: O(n)

# Runtime: 4448 ms, faster than 5.05% of Python3 online submissions for Maximum Frequency Stack.
# Memory Usage: 22.3 MB, less than 64.04% of Python3 online submissions for Maximum Frequency Stack.
