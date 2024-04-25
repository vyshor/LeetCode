class Solution {
public:
    int longestIdealString(string s, int k) {
        vector<int> dp(26, 0);
        int largest = 0;
        for (char &c : s) {
            int pos = (int) (c - 'a');
            int maxx = 1;

            for (int i = max(0, pos-k); i < min(26, pos+k+1); i++) {
                maxx = max(maxx, dp[i]+1);
            }

            dp[pos] = maxx;
            largest = max(largest, maxx);
        }
        return largest;
    }
};
