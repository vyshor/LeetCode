# Sums Problem
# Given an array of integers, return the smallest set of indices of numbers such that they add up to a target number.
# You may not use the same element twice.

# Examples:
# [1, 2, 6, 3, 17, 82, 23, 234] -> 26
# Solution[3, 6]
#
# [1, 2, 6, 3, 17, 82, 23, 234] -> 40
# Solution[4, 6]
#
# [1, 2, 6, 3, 17, 82, 23, 234] -> 23
# Solution[6]

# This is not your standard coding kata. You are expected to:
#   Complete the task in a single class/function
#   Solve from first principles
#   It needs to be human legible i.e. this is not a challenge to solve in the least amount of code/characters possible
#   Write down all assumptions and limits that you have made (they have not been provided for a reason)
#   Note down the methodology(ies) used to solve the problem
#   You can submit more than 1 solution – one naïve and one more elaborate as a possibility
#   You can use Java, Kotlin, C#, Javascript, Ruby, Python, C/C++, Clojure

import unittest

# Assumptions for Naive Bruteforce Solution
# 1. Target can be any integer, positive/negative/zero, zero would return an empty list
# 2. Smallest set of indices of numbers is assumed to be the smallest number of count of elements in the set of indices
# 3. If no combination of sum of numbers can be given to achieve the target number, a False will be returned instead
# 4. Integers used in the array can be positive, negative or zero

# Algorithm / Solution (Brute Force) [Valid for negative integers]
# 1. Iterate through all the integers in the array
# 2. During the iteration, branch out into two situations, whether to include or exclude the iterated number to be added into the sum
# 3. Store the act of adding the number (represented by 1) or the act of NOT adding the number (represented by 0),
# and update the current sum, total count of integers used for the sum (Store into a dictionary to save processing cost)
# The result from the previous iteration can be used directly, to prevent all the calculation again.
# 4. Check if the sum matches the target number
# 5. If yes, check if it is the smallest number of count of elements used to reach the target number,
# 6. If yes again, replace the current best solution, with the new combination in the form of 1 and 0s binary string.
# 7. Translate the best solution to the a list of indices of the numbers that are included

# Time complexity: O(2^n) for n number of integers in the array
# Space complexity: O(2^n) for n number of integers in the array

# This is the naive solution, where you simply brute force all the combinations to get you optimal answer
# Good thing about this bruteforce solution is that it allows negative integers in the array and target integer
# The memory can be reduced if there is constraints such as all the integers (including target integer) are positive

def subsetSumBrute(arr, target):
    dp = {}
    min_idxcount = -1  # Not set yet
    ans = ''
    # Key: Binary sequence of indices that are included or not,
    # e.g. 1010 (index 0 and index 2 are added, and index 1 and 3 are not added)
    # Value: Tuple of (valsum, idxcount)
    # valsum = sum of the numbers that are included
    # idxcount = number of numbers that are included
    if target == 0:
        return []

    for idx, num in enumerate(arr):
        if idx == 0:
            dp['1'] = (num, 1)
            dp['0'] = (0, 0)
        else:
            for key, val_pair in dp.copy().items():
                del dp[key]
                dp[key + '0'] = val_pair
                valsum, idxcount = val_pair
                valsum += num
                if valsum == target:
                    if min_idxcount == -1 or min_idxcount > idxcount + 1:  # Not set yet or better than previous best solution
                        ans = key + '1'
                        min_idxcount = idxcount + 1
                else:
                    dp[key + '1'] = (valsum, idxcount + 1)

    if not ans:  # No possible solution
        return False
    else:
        # Translating the best solution to list of indices of number that needs to be included
        ans_lst = []
        for idx, bin_val in enumerate(ans):
            if bin_val == '1':
                ans_lst.append(idx)
        return ans_lst


# Assumptions for Dynamic Programming Solution
# 1. Target must be non-negative integer, positive/zero, zero would return an empty list
# 2. Smallest set of indices of numbers is assumed to be the smallest number of count of elements in the set of indices
# 3. If no combination of sum of numbers can be given to achieve the target number, a False will be returned instead
# 4. All integers used in the array must be positive
#
# Algorithm / Solution (Dynamic Programming) [Valid for positive integers only]
# 1. Create a (n) x (target + 1) matrix (saved in a dictionary format)
#  Take arr = [5, 3, 1], target = 4 as example
#          0 1 2 3 4
#       5
#       3
#       1
# 2. Fill column 0 with True, since attaining target 0 as sum is possible with any numbers
#          0 1 2 3 4
#       5  T
#       3  T
#       1  T
# 3. For the first row, just check if the column number equals to the target number,a nd fill up the row
#          0 1 2 3 4
#       5  T F F F F
#       3  T
#       1  T
# 3. For each integer in the array (each subsequent row)
#   3.1 For each column number, if the column integer is smaller than the current row integer, copy the True/False from above cell
#          0 1 2 3 4
#       5  T F F F F
#       3  T F F
#       1  T
#   3.2 If the column integer equals to current row integer, return True, and append the index of the row integer (in the original list into the cell)
#   i.e. (True, [1]), since 3 has an index of 1 in [5,3,1]
#          0 1 2 3 4
#       5  T F F F F
#       3  T F F T
#       1  T
#   3.3 Else if the cell above (the current to-be-filled) is True, return True, and solution array + [current row index] from the cell above
#   3.4 Otherwise, copy True/False and the solution array  + [current row index] from the cell at [row index of one row above][current column number - current row value]
#          0 1 2 3 4
#       5  T F F F F
#       3  T F F T F
#       1  T T F T
#   3.5 If both 3.3 and 3.4 return True, then compare which solution array is shorter, and keep the shorter array
#          0 1 2 3 4
#       5  T F F F F
#       3  T F F T F
#       1  T T F T T
# 4. The solution can for the target value, with the smallest subset can be found at [last row index][last column index], if there exists a solution
# 5. Else, False will be returned
#
# Time complexity: O(n * t) for n number of integers in the array, and t for the value of the target integer
# Space complexity: O(n * t) for n number of integers in the array, and t for the value of the target integer
#
# This is the bottom-up dynamic programming approach which builds up the possible combination to obtain the targeted value

def subsetSumDP(arr, target):
    dp = {}

    if target == 0:
        return []

    if not len(arr):
        return False

    for num in arr:
        dp[(0, num)] = (True, [])

    for idx, num in enumerate(arr):
        for i in range(1, target+1):
            if idx == 0:
                dp[(i, num)] = (i == num, [idx] if i == num else [])
            elif i == num:
                dp[(i, num)] = (True, [idx])
            elif i < num:
                dp[(i, num)] = dp[(i, arr[idx-1])]
            else:
                existing_solution = dp.get((i, arr[idx-1]))[0]
                existing_solution_lst = []
                if existing_solution:
                    existing_solution_lst = dp.get((i, arr[idx-1]))[1]

                new_solution, new_solution_lst = dp[(i - num, arr[idx - 1])]
                if new_solution:
                    new_solution_lst = new_solution_lst + [idx]

                if existing_solution and not new_solution:
                    new_solution = existing_solution
                    new_solution_lst = existing_solution_lst

                if existing_solution and new_solution \
                        and len(existing_solution_lst) < len(new_solution_lst):
                    new_solution_lst = existing_solution_lst

                dp[(i, num)] = (new_solution, new_solution_lst)

    current_ans_bool, answerlst = dp[(target, arr[-1])]

    return sorted(answerlst) if current_ans_bool else current_ans_bool


class TestCases(unittest.TestCase):

    funcToTest = [subsetSumBrute,subsetSumDP]

    def test_0(self):  # Edge case
        for func in self.funcToTest:
            arr = [1, 2, 6, 3, 17, 82, 23, 234]
            target = 999
            result = False
            self.assertEqual(result, func(arr, target))

    def test_1(self):
        for func in self.funcToTest:
            arr = [1, 2, 6, 3, 17, 82, 23, 234]
            target = 26
            result = [3, 6]
            self.assertEqual(result, func(arr, target))

    def test_2(self):
        for func in self.funcToTest:
            arr = [1, 2, 6, 3, 17, 82, 23, 234]
            target = 40
            result = [4, 6]
            self.assertEqual(result, func(arr, target))

    def test_3(self):
        for func in self.funcToTest:
            arr = [1, 2, 6, 3, 17, 82, 23, 234]
            target = 23
            result = [6]
            self.assertEqual(result, func(arr, target))

    def test_4(self):
        for func in self.funcToTest:
            arr = [5, 3, 1]
            target = 4
            result = [1, 2]
            self.assertEqual(result, func(arr, target))

    def test_5(self):  # Edge case
        for func in self.funcToTest:
            arr = [1, 2, 6, 3, 17, 82, 23, 234]
            target = 999
            result = False
            self.assertEqual(result, func(arr, target))

    def test_6(self):  # Edge case
        for func in self.funcToTest:
            arr = [1,2]
            target = 0
            result = []
            self.assertEqual(result, func(arr, target))

    def test_7(self):
        for func in self.funcToTest:
            arr = [2,3,7,8,10]
            target = 11
            result = [1,3]
            self.assertEqual(result, func(arr, target))


if __name__ == '__main__':
    unittest.main()





