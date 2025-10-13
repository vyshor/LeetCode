class Solution {
public:
    vector<string> removeAnagrams(vector<string>& words) {
        vector<string> results;
        vector<int> prev(26, 0);
        for (string& word: words) {
            vector<int> counter(26, 0);
            for (char ch: word) {
                counter[ch-97]++;
            }
            bool is_diff = false;
            for (int i = 0; i < 26; i++) {
                if (counter[i] != prev[i]) is_diff = true;
            }

            if (!is_diff) continue;
            prev = std::move(counter);
            results.push_back(word);
        }
        return results;
    }
};
