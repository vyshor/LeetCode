class Solution {
public:
    unordered_map<char, int> op_map = {
        {'+', 0},
        {'-', 1},
        {'*', 2}
    };

    vector<int> nums;
    vector<int> ops;
    unordered_map<int, vector<int>> dp;

    vector<int> recur(int i, int j) {
        int key = (i << 16) | j;
        if (i == j) return {nums[i]};
        if (dp.contains(key)) return dp[key];
        vector<int> results;
        for (int k = i; k < j; k++) {
            auto left_result = recur(i, k);
            auto right_result = recur(k+1, j);
            int op = ops[k];
            for (int k2 = 0; k2 < left_result.size(); k2++) {
                for (int k3 = 0; k3 < right_result.size(); k3++) {
                    int val = 0;
                    switch (op) {
                        case 0:
                            val = left_result[k2]+right_result[k3];
                            break;
                        case 1:
                            val = left_result[k2]-right_result[k3];
                            break;
                        default:
                            val = left_result[k2]*right_result[k3];
                            break;
                    }
                    results.push_back(val);
                }
            }
        }
        dp[key] = std::move(results);
        return dp[key];
    }

    vector<int> diffWaysToCompute(string expression) {
        int n = expression.size();
        stringstream ss;
        int i = 0;
        while (i < n) {
            char ch = expression[i];
            if (op_map.contains(ch)) {
                nums.push_back(std::atoi(ss.str().c_str()));
                ops.push_back(op_map[ch]);
                ss.str("");
            } else {
                ss << ch;
            }
            i++;
        }
        nums.push_back(std::atoi(ss.str().c_str()));
        return recur(0, nums.size() - 1);
    }
};
