class Solution {
public:
    string breakPalindrome(string palindrome) {
        int n = palindrome.size();
        if (n == 1) return "";
        int mid = n/2;

        for (int i = 0; i < mid+1; i++) {
            int ch = palindrome[i];
            if (ch != 97) {
                if (i == mid && (n & 1) == 1) break;

                palindrome[i] = 97;
                return palindrome;
            }
        }
        palindrome[n-1] = 98;
        return palindrome;
    }
};
