class Solution {
public:
    int gcd(int a, int b) {
        if (a > b) {
            return gcd(b, a);
        }

        if (a == 0) return b;
        return gcd(b % a, a);
    }

    int minOperations(vector<int>& nums) {
        int n = nums.size();
        int minn = INT_MAX;
        int ones = 0;
        for (int i = 0; i < n; ++i) {
            int num = nums[i];
            ones += (num == 1);

            int div = num;
            for (int j=i+1; j < n; ++j) {
                div = gcd(div, nums[j]);

                if (div == 1) {
                    minn = min(minn, j-i+(n-1));
                    break;
                }
            }
        }

        if (ones) return n-ones;
        if (minn == INT_MAX) return -1;
        return minn;
    }
};
