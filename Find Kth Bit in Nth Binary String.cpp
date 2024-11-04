class Solution {
public:
    bool recur(int m, int j) {
        if (j == 1) return false;

        int x = 1 << (m-1);
        if (j == x) return true;
        if (j > x) return !recur(m-1, 2*x-j);

        int y = j;
        for (int i = 1; i < m; i++) {
            int minus = 1 << (i-1);
            if (y - minus <= 0) return recur(i, j);
            y -= minus;
        }
        return 0;
    }

    char findKthBit(int n, int k) {
        return char((int) recur(n, k) + 48);
    }
};
