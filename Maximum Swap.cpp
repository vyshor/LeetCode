class Solution {
public:
    int maximumSwap(int num) {
        string nums = to_string(num);
        int n = nums.size(), i = 1, spot = 0, j = 0;
        bool found = false;
        char maxx = '0';
        while (i < n) {
            if (!found) {
                if (nums[i] > nums[i-1]) {
                    found = true;
                    maxx = nums[i];
                    j = i;
                } else if (nums[i] < nums[i-1]) spot = i;
            } else {
                if (nums[i] >= maxx) {
                    maxx = nums[i];
                    j = i;
                }
            }
            i++;
        }

        if (found) {
            i = 0;
            while (i < spot) {
                if (nums[i] < maxx) spot = i;
                i++;
            }
            swap(nums[spot], nums[j]);
        } else return num;
        return stoi(nums);
    }
};
