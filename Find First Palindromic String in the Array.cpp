class Solution {
public:
    string firstPalindrome(vector<string>& words) {
        for (string & word: words) {
            int n = word.size();
            int i = 0;
            int j = n-1;
            bool palindrome = true;
            while (i < j) {
                if (word[i] == word[j]) {
                    i++;
                    j--;
                } else {
                    palindrome = false;
                    break;
                }
            }
            if (palindrome) return word;
        }
        return "";
    }
};
