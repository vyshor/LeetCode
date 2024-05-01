class Solution {
public:
    string reversePrefix(string word, char ch) {
        int i = word.find(ch);
        if (-1 == i) return word;

        stringstream ss;
        for (int j = i; j >= 0; j--) {
            ss << word[j];
        }
        ss << word.substr(i+1);
        return ss.str();
    }
};

