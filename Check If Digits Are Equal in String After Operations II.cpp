class Solution {
public:
    vector<int> factorial = {1, 1, 2, 6, 24, 120};
    vector<vector<int>> crt = {{0,6,2,8,4},{5,1,7,3,9}};

    int ncmod(int n, int c, int mod) {
        // cout << "n=" << n << " c=" << c << " mod=" << mod << endl;
        // n > c
        vector<int> nmod;
        vector<int> cmod;
        while (n > 0) {
            nmod.push_back(n % mod);
            n /= mod;
        }

        cmod.reserve(nmod.size());
        while (c > 0) {
            cmod.push_back(c % mod);
            c /= mod;
        }

        if (cmod.size() < nmod.size()) cmod.resize(nmod.size(), 0);

        int result = 1;
        int m = nmod.size();
        for (int i = 0; i < m; i++) {
            // cout << "nmod[i]=" << nmod[i] << " cmod[i]=" << cmod[i] << endl;
            if ((nmod[i] == 0 && cmod[i] > 0) || (cmod[i] > nmod[i])) {
                result = 0;
                break;
            }
            result *= factorial[nmod[i]] / factorial[cmod[i]] / factorial[nmod[i]-cmod[i]];
        }
        // cout << "Result=" << result % mod << endl;
        return result % mod;
    }

    bool hasSameDigits(string s) {
        int n = s.size();
        vector<int> pascal(n-1, 1);
        int val = 1;
        int j = n-3;
        for (int i = 1; i <= j; i++) {
            // Pascal triangle of height n-1
            int nc2 = ncmod(n-2, i, 2);
            int nc5 = ncmod(n-2, i, 5);

            pascal[i] = crt[nc2][nc5];
            pascal[j] = pascal[i];
            j--;
        }

        // cout << "Pascal= ";
        // for (int i = 0; i < n-1; i++) {
        //     cout << pascal[i] << " ";
        // }
        // cout << endl;

        int left = 0, right = 0;
        for (int i = 0; i < n-1; i++) {
            left += pascal[i]*(s[i]-47);
            right += pascal[i]*(s[i+1]-47);
        }
        return (left % 10) == (right % 10);

    }
};
