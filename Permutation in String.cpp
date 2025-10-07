class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        unordered_map<int, int> counter;
        int total = s1.size();
        for (char ch: s1) {
            counter[ch]++;
        }
        auto original = counter;
        int n = s2.size();
        int left = 0, right = 0;
        while (right < n) {
            int ch = s2[right];
            if (!counter.contains(ch)) {
                right++;
                left = right;
                counter = original;
                continue;
            } else {
                counter[ch]--;
                while (counter[ch] < 0) {
                    counter[s2[left]]++;
                    left++;
                }

                if (right-left+1 == total) return true;
            }
            right++;
        }
        return false;
    }
};
