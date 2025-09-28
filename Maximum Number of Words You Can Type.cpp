class Solution {
public:
    int canBeTypedWords(string text, string brokenLetters) {
        const char* ptr = text.c_str();
        const char* broken = brokenLetters.c_str();
        unordered_set<char> b;
        b.reserve(brokenLetters.size());
        while (*broken != '\0') {
            b.insert(*broken);
            broken++;
        }
        int count = 0;
        int valid_word = 1;
        while (*ptr != '\0') {
            if (*ptr == ' ') {
                count += int(valid_word);
                valid_word = 1;
            } else {
                valid_word &= int(!b.contains(*ptr));
            }
            ptr++;
        }
        return count + valid_word;
    }
};
