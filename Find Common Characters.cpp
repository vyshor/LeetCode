class Solution {
public:
    vector<int> count(string word) {
        vector<int> counter(26, 0);
        for (char&c : word) {
            counter[(int) c - 97]++;
        }
        return counter;
    }
    vector<string> commonChars(vector<string>& words) {
        vector<int> counter = count(words[0]);
        int n = words.size();

        for (int i = 1; i < n; i++) {
            vector<int> counter2 = count(words[i]);
            for (int j = 0; j < 26; j++) {
                counter[j] = min(counter[j], counter2[j]);
            }
        }

        vector<string> ans;
        for (int i = 0; i < 26; i++) {
            for (int j = 0; j < counter[i]; j++) {
                string str(1, (char) (i+97));
                ans.push_back(str);
            }
        }
        return ans;
    }
};
