class Solution {
public:
    int maxSubstrings(string word) {
        int n = word.size();
        vector<deque<int>> prev_idx(26);
        vector<int> dp(n+1, 0);

        for (int i = 0; i < n; i++) {
            int ch = word[i] - 97;
            auto& q = prev_idx[ch];
            while (q.size() >= 2) {
                if (i - q[1] >= 3) q.pop_front();
                else break;
            }

            dp[i+1] = dp[i];
            if (q.size() > 0) {
                int j = q.front();
                if (i-j >= 3) {
                    dp[i+1] = max(dp[i+1], dp[j]+1);
                }
            }
            q.push_back(i);
        }
        return dp[n];

    }
};
