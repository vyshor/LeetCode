class Solution {
public:
    int maxOperations(string s) {
       int n = s.size();
       int seen_zero = 0;
       int total = 0;
       int count = 0;
       for (int i = 0; i < n; ++i) {
            if (s[i] == '1') {
                if (seen_zero) {
                    total += count;
                }
                ++count;
                seen_zero = 0;
            } else {
                seen_zero = 1;
            }
       }

        if (seen_zero) {
            total += count;
        }
        return total;
    }
};
