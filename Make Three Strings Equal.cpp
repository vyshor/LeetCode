class Solution {
public:
    int findMinimumOperations(string s1, string s2, string s3) {
        int n1 = s1.size(), n2 = s2.size(), n3 = s3.size();
        int minn = min(min(n1, n2), n3);
        int maxx = -1;
        for (int i = 0; i < minn; i++) {
            if (s1[i] != s2[i] || s2[i] != s3[i]) {
                maxx = i;
                break;
            }
        }
        if (maxx == 0) return -1;
        if (maxx == -1) maxx = minn;
        return n1+n2+n3-(maxx)*3;
    }
};
