class Solution {
public:
    int compare(string& wordA, string& wordB) {
        if (wordA.size() > wordB.size()) return false;
        int i = 0, j = wordB.size() - wordA.size();
        while (i < wordA.size()) {
            if (wordA[i] != wordB[i] || wordA[i] != wordB[j])
            return 0;
            i++;
            j++;
        }
        return 1;
    }
    int countPrefixSuffixPairs(vector<string>& words) {
        int n = words.size();
        int count = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < i; j++) {
                count += compare(words[j], words[i]);
            }
        }
        return count;
    }
};