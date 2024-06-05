class Solution {
public:
    int longestPalindrome(string s) {
        int odd_count = 0, even_count = 0;
        unordered_map<char, int> counter;
        for (char& c : s) {
            if (!counter.contains(c)) {
                counter[c] = 1;
            } else {
                counter[c]++;
            }

            if (counter[c] % 2 == 0) {
                even_count++;
                odd_count--;
            } else {
                odd_count++;
            }
        }

        if (odd_count > 1) odd_count = 1;
        return even_count*2 + odd_count;
    }
};
