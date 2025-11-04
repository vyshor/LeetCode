class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> counter;
        for (int num: nums) {
            counter[num]++;
        }

        vector<pair<int, int>> arr;
        for (auto [val, count]: counter) {
            arr.emplace_back(-count, val);
        }

        partial_sort(arr.begin(), arr.begin()+k, arr.end());
        vector<int> ans;
        for (int i = 0; i < k; i++) {
            ans.push_back(arr[i].second);
        }
        return ans;
    }

};
