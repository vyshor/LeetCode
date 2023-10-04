class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        n = len(num)
        if n == 1:
            if target == int(num):
                return [num]
            return []

        ans = []
        path = [num[0]]

        def pickOp(i, leading_zero):
            nonlocal ans, path

            for op in ['+', '-', '*', '']:
                if leading_zero and op == "":
                    continue

                path.append(op)
                path.append(num[i])

                if i + 1 == n:
                    ops = ''.join(path)
                    evaluation = eval(ops)
                    if evaluation == target:
                        ans.append(ops)
                else:
                    pickOp(i + 1, num[i] == "0" and op != "")

                path.pop()
                path.pop()

        pickOp(1, path[0] == "0")
        return ans
