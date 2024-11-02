class Solution {
public:
    bool isCircularSentence(string sentence) {
        int n = sentence.size();
        auto ptr = reinterpret_cast<char*>(&sentence[0]);
        auto word = ptr;
        for (int i = 0; i < n; i++) {
            if (*ptr == ' ') {
                if (*(ptr+1) != *(ptr-1)) return false;
            }
            ptr++;
        }
        return (*word == *(ptr-1));
    }
};
