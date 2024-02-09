class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for num in asteroids:
            if not stack:
                stack.append(num)
            elif (num > 0 and stack[-1] > 0) or (num < 0 and stack[-1] < 0):
                stack.append(num)
            elif (num > 0 and stack[-1] < 0):
                stack.append(num)
            else:
                while stack:
                    opp = stack.pop()

                    if (opp < 0 and num < 0) or (opp > 0 and num > 0):
                        stack.append(opp)
                        stack.append(num)
                        break

                    result = num + opp
                    if result == 0:
                        break
                    if (num > 0 and result > 0) or (num < 0 and result < 0):
                        if stack:
                            continue
                        else:
                            stack.append(num)
                            break
                    else:
                        stack.append(opp)
                        break
        return stack


