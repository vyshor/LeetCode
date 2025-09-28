class Solution {
public:
    long long flowerGame(int n, int m) {
        int64_t count = 0;
        for (int i = 3; i < n+m+1; i += 2) {
            int n2 = min(n, i-1);
            int m2 = min(m, i-1);
            count += max(n2-(i-m2)+1, 0);
            // cout << "i " << i << " count: " <<  count << endl;
        }
        return count;
    }
};
