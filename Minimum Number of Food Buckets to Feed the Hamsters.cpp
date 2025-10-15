class Solution {
public:
    int minimumBuckets(string hamsters) {
        int n = hamsters.size();
        // food, empty = i, j
        // fed, hungry = k, m
        int i = 0, j = 0, k = 0, m = 0;
        char prev = hamsters[0];
        if (hamsters[0] == '.') {
            i = 1;
        } else {
            k = INT_MAX;
        }
        for (int v = 1; v < n; v++) {
            // cout << "i: " << i << " j: " << j << " k: "<< k << " m: " << m << endl;
            char cur = hamsters[v];
            if (prev == '.' && cur == '.') {
                int i2 = 1+min(i,j);
                int j2 = min(i,j);
                i = i2;
                j = j2;
            } else if (prev == 'H' && cur == '.') {
                int i2 = 1+min(k,m);
                int j2 = k;
                i = i2;
                j = j2;
            } else if (prev == 'H' && cur == 'H') {
                if (k == INT_MAX) return -1;
                int k2 = INT_MAX;
                int m2 = k;
                k = k2;
                m = m2;
            } else {
                int k2 = i;
                int m2 = min(i, j);
                k = k2;
                m = m2;
            }
            prev = cur;
        }

        if (prev == '.') return min(i, j);
        if (k == INT_MAX) return -1;
        return k;
    }
};
