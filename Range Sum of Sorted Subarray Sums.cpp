class Solution {
public:
    int rangeSum(vector<int>& nums, int n, int left, int right) {
        int MOD = 1000000007;
        vector<int> prefix(n+1, 0);
        vector<int> suffix(n+1, 0);
        int summ = 0;
        for (int i = 0; i < n; i++) {
            summ += nums[i];
            prefix[i+1] = summ;
        }

        int total = summ;
        summ = 0;
        for (int i = n-1; i >= 0; i--) {
            summ += nums[i];
            suffix[i] = summ;
        }

        vector<int> arr;
        arr.reserve(n*n / 2);
        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                arr.push_back(total-prefix[i]-suffix[j+1]);
            }
        }

        sort(arr.begin(), arr.end());
        summ = 0;
        for (int i = left-1; i < right; i++) {
            summ += arr[i];
            summ %= MOD;
        }
        return summ;
    }
};
