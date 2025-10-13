std::unordered_map<char, int> mapping;

class Solution {
public:
    Solution() {
        if (mapping.size() == 0) {
            string row1 = "qwertyuiop";
            string row2 = "asdfghjkl";
            string row3 = "zxcvbnm";
            vector<string> rows = {row1, row2, row3};
            for (int i = 0; i < 3; i++) {
                for (char ch: rows[i]) {
                    mapping[ch] = (1 << i);
                    mapping[ch-32] = (1 << i);
                }
            }
        }
    }

    int bitcount(int i) {
        return (i >> 2) + ((i >> 1) & 1) + (i & 1);
    }

    vector<string> findWords(vector<string>& words) {
        vector<string> ans;
        for (string& word: words) {
            int rows_used = 0;
            for (char ch: word) {
                rows_used |= mapping[ch];
            }
            if (bitcount(rows_used) == 1) ans.push_back(std::move(word));
        }
        return ans;
    }
};

