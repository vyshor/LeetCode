class Solution {
public:
    int countSubstrings(string check_str) {
        s = check_str;
        n = check_str.size();
        for (int i = 0; i < n; i++) {
            checkPalindrome(i, i);
            checkPalindrome(i, i+1);
        }
        return count;
    }
private:
    int count = 0;
    int n;
    string s;
    unordered_map<int, bool> dp;

    bool checkChar(int i, int j) {
        int key = i << 16 | j;
        auto found = dp.find(key);
        if (found == dp.end()) {
            bool value = (s.at(i) == s.at(j));
            dp.insert(make_pair(key, value));
            return value;
        } else {
            return found->second;
        }
    }

    void checkPalindrome(int i, int j) {
        if (i >= 0 && j < n && checkChar(i, j)) {
            count++;
            checkPalindrome(--i, ++j);
        }
    }
};
