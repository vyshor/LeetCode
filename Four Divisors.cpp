class Solution {
public:
    int divisorSum(int num) {
        if (num == 1) return 0;
        int second_pair = 0;
        int upper_limit = num / 2;
        int summ = 1 + num;
        for (int i{2}; i < upper_limit; ++i) {
            if ((num % i) == 0) {
                if (second_pair) return 0;
                second_pair = 1;
                upper_limit = num / i;
                if (upper_limit == i) return 0;
                summ += i + upper_limit;
            }
        }

        return second_pair ? summ : 0;
    }

    int sumFourDivisors(vector<int>& nums) {
        int ans{0};
        unordered_map<int, int> dp;
        for (int num: nums){
            if (dp.contains(num)) ans += dp[num];
            else {
                dp[num] = divisorSum(num);
                ans += dp[num];
            }
        }
        return ans;
    }
};
