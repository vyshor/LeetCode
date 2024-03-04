class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int maxx = 0;
        int maxx2 = 0;
        for (auto & num: nums) {
            if (num >= maxx) {
                maxx2 = maxx;
                maxx = num;
            } else if (num > maxx2) {
                maxx2 = num;
            }
        }
        return (maxx-1)*(maxx2-1);
    }
};
