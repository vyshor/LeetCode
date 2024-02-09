class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        prev = 1
        stack = []
        for num in target:
            if num != prev:
                for _ in range(num-prev):
                    stack.append("Push")
                    stack.append("Pop")

            stack.append("Push")
            prev = num+1

        return stack
