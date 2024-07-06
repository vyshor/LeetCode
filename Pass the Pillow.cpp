class Solution {
public:
    int passThePillow(int n, int time) {
        time %= (2*n-2);
        return (2*n-time-1)*(time >= n) + (time+1)*(time < n);
    }
};
