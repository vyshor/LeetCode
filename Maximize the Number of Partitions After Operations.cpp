class Solution {
public:
    unordered_map<int, int> dp;
    string S;
    int N;
    int K;

    int recur(int i, int changed, int unique) {
        if (unique == K) return 1+recur(i, changed, 0);
        if (i == N) return unique;

        // int i2 = i;

        int key = (i << 2) | (changed << 1) | unique;
        if (dp.contains(key)) return dp[key];

        vector<int> counter(26, 0);
        int maxx = 1;
        int change = 0;

        while (i < N) {
            int ch = S[i]-97;
            unique += (counter[ch] == 0);
            if (unique > K) {
                maxx = max(maxx, 1+recur(i, changed, 0));
                break;
            }

            counter[ch]++;
            if ((changed == 0) && (change == 0) && (counter[ch] > 1)) {
                change = 1;
            }

            if ((unique+change) > K) {
                if (counter[ch] > 1) {
                    // i = 2, k =2
                    // abb.. -> ab|*

                    // There is a special condition here
                    // If K >= 13, * cannot be guaranteed to be unique for both sides
                    // It will always be a duplicate on the subsequent sequence
                    if (K < 13) {
                        maxx = max(maxx, 1+recur(i+1, 1, 1));
                    } else {
                        maxx = max(maxx, 1+recur(i, 1, 0));
                    }

                    // This should be trivial case though, should be covered by before
                    // abb.. -> a*|b
                    // maxx = max(maxx, 1+recur(i, 1, 0));
                }
                // i = 2, k = 2
                // aab.. -> *a|b
                // aab.. -> a*|b
                maxx = max(maxx, 1+recur(i, 1, 0));
            }

            // Special case where abb -> a*|b
            // i is on *
            if ((changed == 0) && (unique ==  K)) {
                maxx = max(maxx, 1+recur(i+1, 1, 0));
            }

            i++;
        }

        dp[key] = maxx;
        // cout << "i=" << i2 << " Maxx: " << maxx << endl;
        return maxx;
    }

    int maxPartitionsAfterOperations(string s, int k) {
        N = s.size();
        S = std::move(s);
        K = k;
        if (k == 26) return 1;

        return recur(0, 0, 0);
    }
};
