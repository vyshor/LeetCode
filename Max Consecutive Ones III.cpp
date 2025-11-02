class Solution {
public:
    int longestOnes(vector<int>& nums, int k) {
        int right = 0, left = 0;
        int n = nums.size();
        int flips = 0;
        int maxx = 0;
        while (right < n) {
            flips += (nums[right] ^ 1);
            while (flips > k) {
                flips -= nums[left] ^ 1;
                left++;
            }
            maxx = max(maxx, right-left+1);
            right++;
        }
        return maxx;
    }
};