class Solution {
public:
    int numberOfAlternatingGroups(vector<int>& colors, int k) {
        int n = colors.size();
        colors.reserve(n+k);
        for (int i = 0; i < k-1; i++) {
            colors.push_back(colors[i]);
        }
        int m = n+k-1;
        int i = 1;
        int count = 0;
        int prev = colors[0];
        int combo = 1;
        while (i < m) {
            if ((colors[i] ^ prev) != 1) {
                combo = 1;
            } else {
                combo++;
            }

            if (combo >= k) count++;

            prev = colors[i];
            i++;
        }
        return count;
    }
};
