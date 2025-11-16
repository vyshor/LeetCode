class Solution {
public:
    int possibleStringCount(string word) {
        int ans = 0;
        char prev = '\0';
        int count = 0;
        for (char ch: word) {
            if (ch != prev) {
                ans += count;
                count = 0;
                prev = ch;
            } else {
                ++count;
            }
        }
        ans += count;
        return ans+1;
    }
};
