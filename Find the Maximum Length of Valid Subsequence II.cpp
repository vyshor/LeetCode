class Solution {
public:
    int maximumLength(vector<int>& nums, int k) {
        vector<int> count(k*k, 0);
        for (int num: nums) {
            int r = num % k;
            count[k*r+r] += 1;

            for (int j = 0; j < k; j++) {
                if (j == r) continue;
                count[k*j+r] += (count[k*j+r] ^ 1) & 1;
            }

            for (int j = 0; j < k; j++) {
                if (j == r) continue;
                count[k*r+j] += count[k*r+j] & 1;
            }
        }
        return max(*max_element(count.begin(), count.end()), 2);
    }
};
