class Solution {
public:
    string s;
    vector<int> counter = vector<int>(7, 0);
    int minn = INT_MAX;

    void recur(int num, int i, int alr_larger) {
        if (i == s.size()) {
            int valid = alr_larger;
            for (int j = 1; j <= 6; j++) {
                valid &= (counter[j] == 0 || counter[j] == j);
            }

            if (valid) {
                minn = min(minn, num);
            }

            return;
        }

        num *= 10;
        int remaining = s.size() - i;
        if (!alr_larger) {
            int limit = s[i]-48;
            for (int j = 1; j <= 6; j++) {
                // Quota allows
                if (counter[j] + remaining >= j && (counter[j]+1) <= j && j >= limit) {
                    counter[j]++;
                    recur(num + j, i+1, j > limit);
                    counter[j]--;
                }
            }
        } else {
            for (int j = 1; j <= 6; j++) {
                // Quota allows
                if (counter[j] + remaining >= j && (counter[j]+1) <= j) {
                    counter[j]++;
                    recur(num + j, i+1, alr_larger);
                    counter[j]--;
                }
            }
        }
    }

    int nextBeautifulNumber(int n) {
        s = to_string(n);
        recur(0, 0, 0);
        if (minn == INT_MAX) {
            counter[1] = 1;
            recur(1, 0, 1);

            counter[1] = 0;
            counter[2] = 1;
            recur(2, 0, 1);
        }
        return minn;
    }
};
