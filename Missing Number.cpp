class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int n = nums.size();
        nums.push_back(0);
        for (int i=0; i<n; i++) nums.at(nums.at(i) % (n+1)) += n+1;
        for (int i=0; i<n; i++) {
            if (nums.at(i) < n+1)
                return i;
        }
        return n;
    }
};
