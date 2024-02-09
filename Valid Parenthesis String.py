class Solution:
    def checkValidString(self, s: str) -> bool:
        lefts = []
        stars = []
        for i, c in enumerate(s):
            if c == "(":
                lefts.append(i)
            elif c == "*":
                stars.append(i)
            else:
                if not lefts and not stars:
                    return False
                elif not lefts:
                    stars.pop()
                else:
                    lefts.pop()

        while lefts:
            if not stars:
                return False
            else:
                if lefts.pop() > stars.pop():
                    return False

        return True
