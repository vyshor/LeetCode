# -----Question 1-----
# Now you are a microbiologist. Initially( when t=0), you have only one bacterium. To perform an important research, you need *exactly* N bacteria.
#
# Every alive bacteria will clone itself every second. Hence, the number of alive bacteria will doubled every second. At every second, you can select any number of bacteria to kill, the killed bacteria will not clone itself anymore, but also cannot be used in the research anymore.
#
# Since the kill operation is expensive, find the minimum number of kill, and the corresponding time (in seconds) to get *exactly* N bacteria.

# -----Solution---------
# The population of the bacteria always follow this series:
# (x - k1) * 2^n + (x - k2) * 2^(n-1) + ..., where n represents the seconds of the time lapsed
#
# And the objective is to minimise the sum of k1 to k(n)
# min(k1, k2, k3, ...)
#
# First, how do we determine n? And how it is related to the population of bacteria, p?
#
# Assuming there is no killing of bacteria
# p = 2*(n), where n represents the seconds lapsed
#
# Hence, in order to achieve a population of N, as given in the question
#
# The minimum time required to reach at least a population of N will require, (ceil(log2(N)) seconds.
# For example, 2^2 < 5 < 2^3
#
# And killing a bacteria in a second earlier, would mean higher bacteria "killed population" as time passes. As the culled population will double every additional seconds.
#
# For example, a population of 5 is required. At least 3 seconds is required, since (ceil(log2(N)). A maximum population of 8 will be achieved if no killing is involved. Thus, a culled population of (8 - 5) = 3 is required by the end of the 3rd second lapsed. The culled population can be represente dby below
#
# 3 = k1* 2^2 + k2 * 2^1 + k3*2^0,
# where k1 represents bacteria killed in first second,
# k2 in second second,
# k3 in third second,
# and k1, k2, k3 are in binary formats (1 or 0).
#
# Thus, to determine the total number kills required is merely conversion of the culled population to a binary format and count the number of 1s, which is in this case, count 1s in (011) = 2
#
# This formula can be extended across various N values.

import math as m

def minkill(N):
    upperbound = m.ceil(m.log2(N))
    killed_expon = 2 ** upperbound - N
    killed_expon_bin = "{0:b}".format(killed_expon)
    kills = killed_expon_bin.count('1')
    return kills, upperbound

test_cases = [
    [8, (0,3)],
    [5, (2,3)],
    [9, (3,4)],
    [12, (1,4)]
]

for idx, (input_N, output) in enumerate(test_cases):
    print("Test Case {} Success: {}".format(idx+1, output == minkill(input_N)))
    assert output == minkill(input_N)

