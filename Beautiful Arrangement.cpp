class Solution {
public:
    vector<vector<int>> choices;
    unordered_map<int, int> dp;
    int N;

    int recur(int i, int used) {
        int key = (i << 15) | used;
        if (dp.contains(key)) return dp[key];

        if (i == N) {
            return 1;
        }

        int summ = 0;
        for (int val: choices[i]) {
            if ((((1 << val) & used) >> val) == 1) continue;

            summ += recur(i+1, ((1 << val) | used));
        }
        dp[key] = summ;
        return summ;
    }

    int countArrangement(int n) {
        N = n;
        choices = vector<vector<int>>(n);
        for (int i = 1; i < n+1; i++) {
            for (int j = i; j < n+1; j++) {
                if ((j % i) == 0) {
                    choices[i-1].push_back(j);
                    if (i != j) choices[j-1].push_back(i);
                }
            }
        }

        return recur(0, 0);
    }
};
