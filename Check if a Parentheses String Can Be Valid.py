class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)
        if n % 2 == 1:
            return False

        unlocked = 0
        opens = 0
        for i in range(n):
            c = s[i]
            if locked[i] == '1':
                if c == "(":
                    opens += 1
                else:
                    if opens >= 1:
                        opens -= 1
                    elif unlocked < 1:
                        return False
                    else:
                        unlocked -= 1
            else:
                unlocked += 1

        unlocked = 0
        opens = 0
        for i in range(n - 1, -1, -1):
            c = s[i]
            if locked[i] == '1':
                if c == ")":
                    opens += 1
                else:
                    if opens >= 1:
                        opens -= 1
                    elif unlocked < 1:
                        return False
                    else:
                        unlocked -= 1
            else:
                unlocked += 1
        return True

# class Solution:
#     def canBeValid(self, s: str, locked: str) -> bool:
#         n = len(s)
#
#         if n % 2 == 1:
#             return False
#
#         free_pt = locked.find('0')
#         if free_pt == -1:
#             free_pt = n
#
#         locked = list(locked)
#         pt = 0
#
#         for i, l in enumerate(locked):
#             if l == '1':
#                 if s[i] == ')':
#                     found_pair = False
#                     for x in range(i, -1, -1):
#                         if locked[x] == '1' and s[x] == '(':
#                             locked[i] = 'X'
#                             locked[x] = 'X'
#                             found_pair = True
#                             break
#
#                     if not found_pair:
#                         for x in range(i, free_pt - 1, -1):
#                             if locked[x] == '0':
#                                 locked[i] = 'X'
#                                 locked[x] = 'X'
#                                 while pt < n and locked[pt] != '0':
#                                     pt += 1
#                                 found_pair = True
#                                 break
#
#                     if not found_pair:
#                         return False
#
#         for i, l in enumerate(locked):
#             if l == '1':
#                 if s[i] == '(':
#                     found_pair = False
#                     for x in range(i + 1, n):
#                         if locked[x] == '1' and s[x] == ')':
#                             locked[i] = 'X'
#                             locked[x] = 'X'
#
#                             found_pair = True
#                             break
#
#                     if not found_pair:
#                         for x in range(i + 1, n):
#                             if locked[x] == '0':
#                                 locked[i] = 'X'
#                                 locked[x] = 'X'
#
#                                 found_pair = True
#                                 break
#
#                     if not found_pair:
#                         return False
#
#         return True
#
