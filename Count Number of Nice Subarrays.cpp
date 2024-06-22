class Solution {
public:
    int numberOfSubarrays(vector<int>& nums, int k) {
        int n = nums.size();
        int count = 0;
        vector<int> prefix, subfix;
        for (int num : nums) {
            if (num % 2) {
                prefix.push_back(count);
                count = 1;
            } else {
                count++;
            }
        }

        if (count) prefix.push_back(count);

        count = 0;
        for (int i = n-1; i > -1; i--) {
            if (nums[i] % 2) {
                subfix.push_back(count);
                count = 1;
            } else {
                count++;
            }
        }

        if (count) subfix.push_back(count);

        int i = k, j = subfix.size()-1, summ = 0;
        while (i < prefix.size()) {
            summ += prefix[i] * subfix[j];
            i++;
            j--;
        }
        return summ;
    }
};
