class Solution {
public:
    long long minTime(vector<int>& skill, vector<int>& mana) {
        int m = mana.size();
        int n = skill.size();
        vector<vector<int64_t>> cost(m, vector<int64_t>(n+1, 0));

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                cost[i][j+1] = cost[i][j] + mana[i] * skill[j];
            }
        }

        for (int i = 1; i < m; i++) {
            int64_t max_diff = 0;
            for (int j = 0; j < n; j++) {
                max_diff = max(max_diff, cost[i-1][j+1] - cost[i][j]);
            }

            cost[i][0] = max_diff;
            for (int j = 0; j < n; j++) {
                cost[i][j+1] += max_diff;
            }
        }

        // for (int i = 0; i < m; i++) {
        //     cout << "i=" << i << " ";
        //     for (int j = 0; j < n+1; j++) {
        //         cout << dp[i][j] << " ";
        //     }
        //     cout << endl;
        // }

        return cost[m-1][n];
    }
};
