class Solution {
public:
    int maxDistance(vector<int>& colors) {
        int n = colors.size();
        int leftmostcolor = colors[0];
        int leftmost2 = -1;
        int rightmostcolor = colors[n-1];
        int rightmost2 = -1;

        if (leftmostcolor != rightmostcolor) return n-1;

        int i = 1;
        while (i < n) {
            if (colors[i] != leftmostcolor) {
                leftmost2 = i;
                break;
            }
            i++;
        }
        i = n-2;
        while (i >= 0) {
            if (colors[i] != rightmostcolor) {
                rightmost2 = i;
                break;
            }
            i--;
        }
        return max(rightmost2, n-1-leftmost2);
    }
};
