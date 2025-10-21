class Solution {
public:
    int maxPalindromesAfterOperations(vector<string>& words) {
        unordered_map<int, int> counter;
        vector<int> arr;
        vector<int> count(26, 0);
        int total_pairs = 0;
        for (string& word: words) {
            int m = word.size();
            // cout << "m=" << m << endl;
            if (!counter.contains(m)) arr.push_back(m);
            counter[m]++;

            for (char ch: word) {
                count[ch-97]++;
                total_pairs += ((count[ch-97] & 1) == 0);
            }
        }

        sort(arr.begin(), arr.end());
        int ans = 0;
        for (int word_size: arr) {
            // cout << word_size << endl;
            int pairs_needed = word_size / 2;
            int word_count = counter[word_size];
            if (pairs_needed == 0) {
                ans += word_count;
            } else {
                if (total_pairs <= (pairs_needed * word_count)) {
                    ans += total_pairs / pairs_needed;
                    return ans;
                } else {
                    total_pairs -= pairs_needed*word_count;
                    ans += word_count;
                }
            }
        }
        return ans;
    }
};
