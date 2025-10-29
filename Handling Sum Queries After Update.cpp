class Solution {
public:
    vector<long long> handleQuery(vector<int>& nums1, vector<int>& nums2, vector<vector<int>>& queries) {
        vector<long long> ans;
        int64_t summ2 = 0;
        for (int64_t num: nums2) {
            summ2 += num;
        }
        bitset<100'000> bits;
        int n = nums1.size();
        for (int i = 0; i < n; i++) {
            bits[i] = nums1[i];
        }

        for (auto& query: queries) {
            if (query[0] == 1) {
                int l = query[1], r = query[2];
                for (int i = l; i < r+1; i++) {
                    bits.flip(i);
                }
            } else if (query[0] == 2) {
                summ2 += int64_t(query[1]) * int64_t(bits.count());
            } else {
                ans.push_back(summ2);
            }
        }
        return ans;
    }
};