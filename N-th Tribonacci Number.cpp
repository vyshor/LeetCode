class Solution {
public:
    int tribonacci(int n) {
        if (n < 2) return n;
        if (n == 2) return 1;

        int n1 = 0, n2 = 1, n3 = 1;
        for (int i = 0; i < n-2; i++) {
            int n4 = n1+n2+n3;
            n1 = n2;
            n2 = n3;
            n3 = n4;
        }

        return n3;
    }
};
