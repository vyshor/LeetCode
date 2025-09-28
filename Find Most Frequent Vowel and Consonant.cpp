class Solution {
public:
    int maxFreqSum(string s) {
        auto ptr = s.c_str();
        int max_freq_const = 0;
        int max_freq_vow = 0;
        unordered_set<int> vowels{'a', 'e', 'i', 'o', 'u'};
        vector<int> counter(26, 0);
        while (*ptr != '\0') {
            bool is_vowel = vowels.contains(*ptr);
            int val = *ptr - 97;
            counter[val]++;
            if (is_vowel) max_freq_vow = max(max_freq_vow, counter[val]);
            else max_freq_const = max(max_freq_const, counter[val]);
            ptr++;
        }
        return max_freq_const + max_freq_vow;
    }
};
