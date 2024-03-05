class Solution {
public:
    int minimumLength(string s) {
        int i = 0;
        int j = s.size()-1;

        while (s[i] == s[j] && i != j) {
            char c = s[i];
            i++;
            while (i <= j && s[i] == c) i++;

            j--;
            while (j >= i && s[j] == c) j--;

            if (j < i) return 0;
        }

        return j-i+1;
    }
};
