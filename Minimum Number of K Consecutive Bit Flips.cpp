class Solution {
public:
    int minKBitFlips(vector<int>& nums, int k) {
        deque<int> q;
        int n = nums.size(), i = 0, count = 0, xorr = 0;
        while (i < n) {
            if (q.size() > 0 && q.front() <= i) {
                q.pop_front();
                xorr ^= 1;
            }

            if (!(nums[i]^xorr)) {
                if (i > n-k) return -1;
                xorr ^= 1;
                count++;
                q.push_back(i+k);
            }
            i++;
        }
        return count;
    }
};

