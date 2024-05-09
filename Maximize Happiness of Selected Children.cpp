class Solution {
public:
    long long maximumHappinessSum(vector<int>& happiness, int k) {
        sort(happiness.begin(), happiness.end());
        int n = happiness.size();
        int64_t count = 0;
        for (int i = 0; i < k; i++) {
            count += max(0, happiness[n-i-1]-i);
        }
        return count;
    }
};