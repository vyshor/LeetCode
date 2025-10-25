class Solution {
public:
    int totalMoney(int n) {
        int c = n / 7;
        int r = n % 7;
        return (c*21+(c*(c+1)*7/2))+(r*(r+1)/2)+(c*r);
    }
};
