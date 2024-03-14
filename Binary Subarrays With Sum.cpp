class Solution {
public:
    int numSubarraysWithSum(vector<int>& nums, int goal) {
        if (goal == 0) {
            int combo = 0;
            int total = 0;
            for (int& num: nums) {
                if (num == 1 && combo > 0) {
                    total += (combo*(combo+1))/2;
                    combo = 0;
                } else if (num == 0) combo++;
            }

            if (combo > 0) total += (combo*(combo+1))/2;
            return total;
        }

        vector<int> arr;
        int combo = 1;
        for (int& num: nums) {
            if (num == 1) {
                arr.push_back(combo);
                combo = 1;
            } else {
                combo++;
            }
        }
        arr.push_back(combo);
        int left = 0;
        int right = goal;
        int total = 0;
        while (right < arr.size()) {
            total += arr.at(right)*arr.at(left);
            right++;
            left++;
        }
        return total;
    }
};