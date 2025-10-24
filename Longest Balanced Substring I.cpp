class Solution {
public:
    int longestBalanced(string s) {
        int n = s.size();
        if (n == 1) return 1;

        int maxx = 0;
        for (int i = 0; i < n-1; i++) {
            int bmax = 0;
            unordered_map<int, int> counter;
            counter[s[i]]++;
            bmax = max(bmax, counter[s[i]]);
            for (int j = i+1; j < n; j++) {
                counter[s[j]]++;
                bmax = max(bmax, counter[s[j]]);
                int balanced = 1;
                for (auto [_, v]: counter) {
                    if (v != bmax) {
                        balanced = 0;
                        break;
                    }
                }
                if (balanced) maxx = max(maxx, j-i+1);
            }
        }
        return maxx;
    }
};
