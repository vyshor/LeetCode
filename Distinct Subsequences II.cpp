class Solution {
public:
    int distinctSubseqII(string s) {
        int MOD = 1e9 + 7;
        vector<int> prev(26, -1);
        vector<int> comb(26, 0);
        int product = 0;
        int n = s.size();
        for (int i = 0; i < n; i++) {
            int ch = s[i] - 97;
            int old_product = product;
            if (prev[ch] != -1) {
                product = (product << 1) - comb[ch];
                if (product < 0) {
                    product += MOD;
                }
                product %= MOD;
            } else {
                product = ((product << 1) + 1) % MOD;
            }
            prev[ch] = i;
            comb[ch] = old_product;
        }
        return product;
    }
};
