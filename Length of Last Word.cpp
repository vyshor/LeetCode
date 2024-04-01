class Solution {
public:
    int lengthOfLastWord(string s) {
        int count = 0;
        bool have_space = true;
        for (char& c : s) {
            if (c == ' ') have_space = true;
            else if (have_space) {
                count = 1;
                have_space = false;
            } else
                count++;
        }
        return count;
    }
};
