class Solution {
public:
    int word2bit(string& word) {
        int bit = 0;
        for (int ch: word) {
            bit |= (1 << (ch-97));
        }
        return bit;
    }
    vector<int> findNumOfValidWords(vector<string>& words, vector<string>& puzzles) {
        unordered_map<int, int> counter;
        for (string& word: words) {
            counter[word2bit(word)]++;
        }

        vector<int> ans;
        for (string& puzzle: puzzles) {
            int pbit = word2bit(puzzle);
            int first_pos = puzzle[0]-97;
            vector<int> valid{1 << first_pos};
            for (int i = 0; i < 26; i++) {
                if (i == first_pos) continue;

                int bit_match = 1 << i;
                if ((pbit & bit_match) == bit_match) {
                    int m = valid.size();
                    for (int j = 0; j < m; j++) {
                        valid.push_back(valid[j] | bit_match);
                    }
                }
            }

            int m = valid.size();
            int count = 0;
            for (int j = 0; j < m; j++) {
                count += counter[valid[j]];
            }
            ans.push_back(count);
        }
        return ans;
    }
};
