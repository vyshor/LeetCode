class Solution {
public:
    int minSwaps(string s) {
        int n = 0, count = 0;
        for (char c: s) {
            if (c == '[') n++;
            else if (n == 0) {
                count++;
                n++;
            } else n--;
        }
        return count;
    }
};
