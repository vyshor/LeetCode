class Solution {
public:
    int minChanges(string s) {
        int count = 0;
        for (int i = 0; i < s.size(); i += 2) {
            count += s[i] != s[i+1];
        }
        return count;
    }
};
