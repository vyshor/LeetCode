class Solution {
public:
    int countPermutations(vector<int>& complexity) {
        int first = complexity[0];
        int n = complexity.size();
        int64_t factorial{1};
        int64_t mod = 1e9 + 7;
        for (int64_t i{1}; i < n; ++i) {
            if (complexity[i] <= first) return 0;
            factorial = (factorial * i) % mod;
        }
        return factorial;
    }
};
