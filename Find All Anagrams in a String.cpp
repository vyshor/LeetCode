class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        unordered_map<int, int> target;
        int target_count = 0;
        for (char ch: p) {
            target[ch]++;
            target_count++;
        }

        int n = s.size();
        vector<int> results;
        unordered_map<int, int> counter = target;
        int counter_count = target_count;
        int left = 0, right = 0;
        while (right < n) {
            char ch = s[right];
            if (!counter.contains(ch)) {
                right++;
                left = right;
                counter = target;
                counter_count = target_count;
                continue;
            }

            counter[ch]--;
            counter_count--;
            while (counter[ch] < 0) {
                counter[s[left]]++;
                counter_count++;
                left++;
            }

            if (counter_count == 0) results.push_back(left);
            right++;
        }
        return results;
    }
};
