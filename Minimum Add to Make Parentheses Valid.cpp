class Solution {
public:
    int minAddToMakeValid(string s) {
        int count = 0, n = 0;
        for (char c: s) {
            if (c == '(') n++;
            else if (n == 0) count++;
            else n--;
        }
        return count + n;
    }
};
