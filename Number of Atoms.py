class Solution:
    def countOfAtoms(self, formula: str) -> str:
        def read(i, n):
            nonlocal formula
            formula_str = ''
            digit_str = ''
            formula_state = True
            counter = Counter()
            while i < n:
                c = formula[i]
                if c == ")":
                    if digit_str == '':
                        digit_str = '1'

                    counter[formula_str] += int(digit_str)
                    digit_str = ''
                    i += 1

                    while i < n:
                        c = formula[i]
                        if c.isdigit():
                            digit_str += c
                        else:
                            break
                        i += 1

                    if digit_str == '':
                        digit_str = '1'

                    m = int(digit_str)
                    for k in counter:
                        counter[k] *= m
                    return counter, i
                elif c == "(":
                    new_counter, i = read(i + 1, n)
                    for k, v in new_counter.items():
                        counter[k] += v
                    continue
                elif c.isdigit():
                    if formula_state:
                        formula_state = False
                        digit_str += c
                    else:
                        digit_str += c
                elif c.isupper():
                    if formula_str:
                        if digit_str == '':
                            digit_str = '1'
                        counter[formula_str] += int(digit_str)
                    formula_str = c
                    digit_str = ''
                else:
                    formula_str += c
                i += 1

            if digit_str == '':
                digit_str = '1'

            counter[formula_str] += int(digit_str)
            # print(counter)
            return counter, i

        counter, _ = read(0, len(formula))
        keys = sorted(counter.keys())
        ans = ''
        # print(keys)

        for key in keys:
            if key:
                if counter[key] == 1:
                    ans += key
                else:
                    ans += key + str(counter[key])
        return ans
