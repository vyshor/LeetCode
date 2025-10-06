class Solution {
public:
    vector<int> arr;
    void count_bit(int a) {
        int i = 0;
        while (a > 0) {
            arr[i] += (a & 1);
            a >>= 1;
            i++;
        }
    }

    int totalHammingDistance(vector<int>& nums) {
        int n = nums.size();
        int total = 0;
        arr = vector<int>(31, 0);

        for (int i = 0; i < n; i++) {
            count_bit(nums[i]);
        }

        for (int i = 0; i < 31; i++) {
            total += arr[i] * (n-arr[i]);
        }

        return total;
    }
};
