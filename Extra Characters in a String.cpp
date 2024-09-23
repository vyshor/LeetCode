class Solution {
public:
    int minExtraChar(string s, vector<string>& dictionary) {
        unordered_map<string, vector<int>> ptrs;
        for (auto word: dictionary) ptrs[word] = {0};
        int n = s.size();
        vector<int> dp(n+1, 0);
        for (int i = 1; i <= n; i++) {
            dp[i] = dp[i-1]+1;
            auto c = s[i-1];
            for (auto [word, all_pos]: ptrs) {
                vector<int> new_pos{0};
                for (int pos: all_pos) {
                    if (word[pos] == c) {
                        pos++;
                        if (pos == word.size()) dp[i] = min(dp[i], dp[i-word.size()]);
                        else new_pos.push_back(pos);
                    }
                }
                ptrs[word] = new_pos;
            }
        }
        return dp.back();
    }
};
