class Solution {
public:
    bool doesAliceWin(string s) {
        const char* ptr = s.c_str();
        int count = 0;
        while (*ptr != '\0') {
            count += (*ptr == 'a' || *ptr == 'e' || *ptr == 'i' || *ptr == 'o' || + *ptr == 'u');
            ptr++;
        }
        return count != 0;
    }
};
