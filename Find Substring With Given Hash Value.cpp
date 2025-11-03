class Solution {
public:
    string subStrHash(string s, int power, int modulo, int k, int hashValue) {
        int n = s.size();
        int64_t hsum = 0;
        int64_t hash = hashValue;
        int64_t mod = modulo;
        int64_t pow = power;
        int64_t mpow = 1;

        for (int i = 0; i < k-1; i++) {
            mpow = (mpow*pow) % mod;
        }

        for (int i = n-1; i >= n-k+1; i--) {
            int64_t ch = s[i]-96;
            hsum = (hsum + ch) % mod;
            hsum = (hsum * pow) % mod;
        }
        hsum = (hsum + s[n-k]-96) % mod;

        string ans;
        if (hsum == hash) ans = s.substr(n-k, k);

        int i = n-k-1;
        while (i >= 0) {
            int64_t ch = s[i]-96;
            int64_t prev_ch = s[i+k]-96;

            hsum -= prev_ch*mpow;
            while (hsum < 0) {
                hsum += (((-hsum)/mod)+1)*mod;
            }
            hsum %= mod;
            hsum = (hsum*pow) % mod;
            hsum = (hsum+ch) % mod;

            if (hsum == hash) ans = s.substr(i, k);

            i--;
        }
        return ans;
    }
};
