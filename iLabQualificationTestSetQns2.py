# -----Question 2-----
# Now you are a NTU student and your final exams are coming. You still have N (1<=N<=1e6) days to study.
#
# But, you procrastinated for the whole semester. Now you need to all of your M (1<=M<=1e6) modules in total! Module i will have a_i(1<=a_i<=1e9) slides you need to study.
#
# Luckily, you met a mystery guy when you were going for lunch. He said he will help you to overcome the procrastination by giving you K magic power. So everyday, you will be able to study *at most* K slides efficiently. But there's a weird restriction, you cannot study two different modules in the same day, otherwise you will forget everything and lose your magic power.
#
# The mystery guy will give you the magic power if you can answer the following question: what is the minimum value of K, such that you can finish studying all of your modules within N days?
#
# You will need to answer the value of the minimum K. If it is impossible, answer -1.
#
# -----Solution---------
# Firstly, since you can only study a module per day, if number of days is less than number of modules, then it is impossible to get minimum K.
#
# As for the minimum K, we just need to sort the modules by the number of slides in descending order, and determine how many minimum number of days for each module if distributed equally, represented by m. We would also have excess days, represented by e = N - M * m. For the excess days, we then distribute the excess days in order of the highest number of slides in each module with most priority.
#
# For example,
# if we have a total of N = 11, the slides for the modules (after sorting) are
# [8, 5, 4, 3, 2]
#
# We would assign two days minimally to each module. And then with an excess days of 1, we assign it to module with 8 slides. We then compare between the highest value divided by the excess days included (module with 8 slides / 3 days) and the highest value divided without the excess days (module with 5 slides / 2 days) to obtain the higher one, and apply a floor function to it to determine the minimum K value.

from math import ceil

def minK(N, M , a):
    if N < M:
        return -1

    num_of_days_per_module = N // M
    excess_days = N % M
    a.sort(reverse=True)
    return max(ceil(a[excess_days-1] / (num_of_days_per_module + 1)) if excess_days else 0, ceil(a[excess_days] / num_of_days_per_module))

test_cases = [
    [5, 5, [3,2,4,8,5], 8],
    [6, 5, [3,2,4,8,5], 5],
    [10, 5, [3,2,4,8,5], 4],
    [11, 5, [3,2,4,8,5], 3]
]

for idx, (input_N, input_M, input_a, output) in enumerate(test_cases):
    print("Test Case {} Success: {}".format(idx+1, output == minK(input_N, input_M, input_a)))
    assert output == minK(input_N, input_M, input_a)



