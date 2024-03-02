class Solution {
public:
    string makeSmallestPalindrome(string s) {
        int j = s.size() - 1;
        int i = 0;

        while (i < j) {
            if (s.at(j) < s.at(i)) {
                s.at(i) = s.at(j);
            } else {
                s.at(j) = s.at(i);
            }
            i++;
            j--;
        }

        return s;
    }
};
