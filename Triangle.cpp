class Solution {
public:
    int minimumTotal(vector<vector<int>>& triangle) {
        int h = triangle.size();
        for (int i = 1; i < h; i++) {
            vector<int> new_dp(i+1, 0);
            triangle[i][0] += triangle[i-1][0];
            triangle[i][i] += triangle[i-1][i-1];
            for (int j = 1; j < i; j++) {
                triangle[i][j] = min(triangle[i-1][j-1], triangle[i-1][j]) + triangle[i][j];
            }
        }

        // for (int i = 0; i < h; i++) {
        //     cout << dp[i] << endl;
        // }
        return *min_element(triangle.back().begin(), triangle.back().end());
    }
};