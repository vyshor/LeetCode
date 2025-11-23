class Solution {
public:
    int maxSumDivThree(vector<int>& nums) {
        int summ{0};
        int minn_two0 = INT_MAX, minn_two1 = INT_MAX, minn_one0 = INT_MAX, minn_one1 = INT_MAX;

        for (int num: nums) {
            summ += num;
            int r = num % 3;
            if (r == 1) {
                if (num < minn_one0) {
                    std::swap(num, minn_one0);
                }
                if (num < minn_one1) {
                    std::swap(num, minn_one1);
                }
            } else if (r == 2) {
                if (num < minn_two0) {
                    std::swap(num, minn_two0);
                }
                if (num < minn_two1) {
                    std::swap(num, minn_two1);
                }
            }
        }

        int total_r = summ % 3;
        if (total_r == 0) return summ;
        if (total_r == 1) {
            if (minn_one0 == INT_MAX && minn_two1 == INT_MAX) return 0;
            if (minn_one0 == INT_MAX) return summ - minn_two0 - minn_two1;
            if (minn_two1 == INT_MAX) return summ - minn_one0;
            return summ - min(minn_one0, minn_two0 + minn_two1);
        }
        if (minn_two0 == INT_MAX && minn_one1 == INT_MAX) return 0;
        if (minn_two0 == INT_MAX) return summ - minn_one0 - minn_one1;
        if (minn_one1 == INT_MAX) return summ - minn_two0;
        return summ - min(minn_two0, minn_one0 + minn_one1);
    }
};
