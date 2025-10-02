class Solution {
public:
    vector<string> splitWordsBySeparator(vector<string>& words, char separator) {
        vector<string> ans;
        stringstream ss;
        int i =0;
        for (string& word: words) {
            const char* c = word.c_str();
            while (*c != '\0') {
                if (*c == separator) {
                    if (i > 0) {
                        i = 0;
                        ans.push_back(ss.str());
                        ss.str("");
                        ss.clear();
                    }
                } else {
                    ss << *c;
                    i++;
                }
                c++;
            }
            if (i > 0) {
                ans.push_back(ss.str());
                ss.str("");
                ss.clear();
                i = 0;
            }
        }
        return ans;
    }
};