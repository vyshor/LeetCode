class Solution {
public:
    bool detectCapitalUse(string word) {
        int all_caps = 1, first_caps = 1, not_caps = 1;
        int n = word.size();
        for (int i = 0; i < n; i++) {
            int caps = (word[i] < 97);
            all_caps &= caps;
            if (i != 0) first_caps &= (caps ^ 1);
            not_caps &= (caps ^ 1);
        }
        return all_caps | first_caps | not_caps;
    }
};
