class Solution {
public:
    int countConsistentStrings(string allowed, vector<string>& words) {
        unordered_set<char> seen(allowed.begin(), allowed.end());
        int count = 0;
        for (auto word: words) {
            bool can = true;
            for (char c: word) {
                if (!seen.contains(c)) {
                    can = false;
                    break;
                }
            }
            if (can) count++;
        }
        return count;
    }
};
