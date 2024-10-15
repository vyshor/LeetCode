class Solution {
public:
    long long minimumSteps(string s) {
        int64_t count = 0;
        int n = s.size(), left = 0, right = 0;
        while (right < n) {
            if (s[right] == '0') {
                count += right-left;
                left++;
            }
            right++;
        }
        return count;
    }
};
