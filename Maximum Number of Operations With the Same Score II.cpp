class Solution {
public:
    int dp[3][2000][2000];
    vector<int> NUMS;

    int recur(int i, int j, int m, int score) {
        if (j < i) return 0;

        if (dp[m][i][j] != -1) return dp[m][i][j];
        if (j-i <= 0) {
            dp[m][i][j] = 0;
            return 0;
        }

        int score0 = NUMS[i] + NUMS[i+1], score1 = NUMS[j-1]+NUMS[j], score2=NUMS[i]+NUMS[j];
        int maxx = 0;
        if (score0 == score) {
            maxx = max(maxx, 1+recur(i+2, j, m, score));
        }
        if (score1 == score) {
            maxx = max(maxx, 1+recur(i, j-2, m, score));
        }
        if (score2 == score) {
            maxx = max(maxx, 1+recur(i+1, j-1, m, score));
        }
        dp[m][i][j] = maxx;
        return maxx;
    }

    int maxOperations(vector<int>& nums) {
        int n = nums.size();
        int score0 = nums[0] + nums[1], score1 = nums[n-2]+nums[n-1], score2=nums[0]+nums[n-1];
        unordered_map<int, int> mapping;
        mapping[score0] = 0;
        if (!mapping.contains(score1)) mapping[score1] = 1;
        if (!mapping.contains(score2)) mapping[score2] = 2;

        NUMS = std::move(nums);

        std::memset(&dp[0][0][0], -1, sizeof(int) * 3 * 2000 * 2000);

        int maxx = recur(0, n-1, mapping[score0], score0);
        maxx = max(maxx, recur(0, n-1, mapping[score1], score1));
        maxx = max(maxx, recur(0, n-1, mapping[score2], score2));

        return maxx;
    }
};
