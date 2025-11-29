class Solution {
public:
    int M;
    int N;
    vector<int> hprefix;
    vector<int> vprefix;
    vector<int> hcut;
    vector<int> vcut;

    int minCost(int i1, int j1, int i2, int j2) {
        if (i1 == i2 && j1 == j2) {
            return 0;
        }

        int maxx = INT_MIN;
        int side_maxx = INT_MIN;
        int cost = INT_MIN;
        int cut_idx = -1;
        int is_hcut = 0;

        for (int i{i1}; i < i2; ++i) {
            int other_side = vprefix[j2] - vprefix[j1];
            int cur_cost = hcut[i];
            if (cur_cost > maxx || (cur_cost == maxx && other_side < side_maxx)) {
                maxx = cur_cost;
                side_maxx = other_side;
                cost = hcut[i];
                cut_idx = i;
                is_hcut = 1;
            }
        }

        for (int j{j1}; j < j2; ++j) {
            int other_side = hprefix[i2] - hprefix[i1];
            int cur_cost = vcut[j];
            if (cur_cost > maxx || (cur_cost == maxx && other_side < side_maxx)) {
                maxx = cur_cost;
                side_maxx = other_side;
                cost = vcut[j];
                cut_idx = j;
                is_hcut = 0;
            }
        }

        // cout << "cut_idx=" << cut_idx << " is_hcut=" << is_hcut << endl;

        if (is_hcut) {
            cost += minCost(i1, j1, cut_idx, j2) + minCost(cut_idx+1, j1, i2, j2);
        } else {
            cost += minCost(i1, j1, i2, cut_idx) + minCost(i1, cut_idx+1, i2, j2);
        }

        return cost;
    }

    int minimumCost(int m, int n, vector<int>& horizontalCut, vector<int>& verticalCut) {
        M = m;
        N = n;
        hprefix = vector<int>(m, 0);
        vprefix = vector<int>(n, 0);
        hcut = std::move(horizontalCut);
        vcut = std::move(verticalCut);
        for (int i{1}; i < m; ++i) {
            hprefix[i] = hprefix[i-1] + hcut[i-1];
        }

        for (int j{1}; j < n; ++j) {
            vprefix[j] = vprefix[j-1] + vcut[j-1];
        }

        return minCost(0, 0, m-1, n-1);
    }
};


class Solution {
public:
    int M;
    int N;
    vector<int> dp;
    vector<int> hcut;
    vector<int> vcut;

    int minCost(int i1, int j1, int i2, int j2) {
        constexpr int offset = 400;
        int key = ((i1 * N + j1) * offset) + (i2 * N + j2);
        if (dp[key] != -1) return dp[key];

        if (i1 == i2 && j1 == j2) {
            dp[key] = 0;
            return 0;
        }

        int minn = INT_MAX;
        for (int i{i1}; i < i2; ++i) {
            minn = min(minn, hcut[i] + minCost(i1, j1, i, j2) + minCost(i+1, j1, i2, j2));
        }

        for (int j{j1}; j < j2; ++j) {
            minn = min(minn, vcut[j] + minCost(i1, j1, i2, j) + minCost(i1, j+1, i2, j2));
        }
        dp[key] = minn;
        return dp[key];
    }

    int minimumCost(int m, int n, vector<int>& horizontalCut, vector<int>& verticalCut) {
        M = m;
        N = n;
        dp = vector<int>(400*400, -1);
        hcut = std::move(horizontalCut);
        vcut = std::move(verticalCut);
        return minCost(0, 0, m-1, n-1);
    }
};
