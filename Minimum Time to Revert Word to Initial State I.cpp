class Solution {
public:
    int minimumTimeToInitialState(string word, int k) {
        int m = word.size();
        if (k > m) return 1;
        int i = k;
        int count = 1;
        while (i < m) {
            int j = i;
            int j2 = 0;
            while (j < m) {
                if (word[j] != word[j2]) break;
                j2++;
                j++;
            }

            if (j == m) return count;
            count++;
            i += k;
        }
        return count;
    }
};
