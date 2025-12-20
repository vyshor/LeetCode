class Solution {
public:
    long long maxProfit(vector<int>& prices, vector<int>& strategy, int k) {
        int n = prices.size();
        vector<int64_t> prefixes(n+1);
        vector<int64_t> suffixes(n+1);

        int64_t summ{0};
        for (int i{0}; i < n; ++i) {
            summ += prices[i] * strategy[i];
            prefixes[i+1] = summ;
        }

        for (int i{0}; i < n+1; ++i) {
            suffixes[i] = summ - prefixes[i];
        }

        int64_t maxx = summ;
        int left = 0, mid = k/2, right = k;
        summ = 0;

        for (int i{mid}; i < right; ++i) {
            summ += prices[i];
        }

        // suffix | zeroes | ones | prefix
        //        |left    |mid   |right

        maxx = max(maxx, prefixes[left]+summ+suffixes[right]);
        while (right < n) {
            maxx = max(maxx, prefixes[left]+summ+suffixes[right]);
            summ += prices[right] - prices[mid];
            ++right;
            ++mid;
            ++left;
        }
        maxx = max(maxx, prefixes[left]+summ+suffixes[right]);
        return maxx;
    }
};
