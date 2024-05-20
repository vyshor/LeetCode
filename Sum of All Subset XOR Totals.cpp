class Solution {
public:
    int subsetXORSum(vector<int>& nums) {
        int n = nums.size();
        int total = 0, xorr=0;
        function<void(int)> explore;
        explore = [&n, &total, &xorr, &explore, &nums] (int i) -> void {
            if (i == n) {
                total += xorr;
                return;
            }

            explore(i+1);

            int prev = xorr;
            xorr ^= nums[i];

            explore(i+1);
            xorr = prev;
        };
        explore(0);
        return total;
    }
};
