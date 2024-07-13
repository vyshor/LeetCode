class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        arr = []
        n = len(positions)
        for i in range(n):
            arr.append((positions[i], i, healths[i], directions[i] == "R"))

        arr.sort()
        stack = []
        ans = [-1] * n
        for i in range(n):
            _, j, h, is_right = arr[i]
            if is_right:
                stack.append([j, h])
            else:
                while stack:
                    if stack[-1][1] == h:
                        h = 0
                        stack.pop()
                        break
                    elif stack[-1][1] > h:
                        h = 0
                        stack[-1][1] -= 1
                        break
                    else:
                        stack.pop()
                        h -= 1

                if h:
                    ans[j] = h

        for (j, h) in stack:
            ans[j] = h

        truncated_ans = []
        for h in ans:
            if h != -1:
                truncated_ans.append(h)
        return truncated_ans
