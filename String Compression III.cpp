class Solution {
public:
    string compressedString(string word) {
        stringstream ss;
        char prev = word[0];
        int count = 0;
        for (char c: word) {
            if (prev == c) {
                count++;
                if (count == 9) {
                    ss << count << prev;
                    count = 0;
                }
            } else {
                if (count > 0) {
                    ss << count << prev;
                }
                prev = c;
                count = 1;
            }
        }

        if (count > 0) {
            ss << count << prev;
        }
        return ss.str();
    }
};
