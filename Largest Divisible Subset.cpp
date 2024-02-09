class Solution {
public:
    vector<int> largestDivisibleSubset(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int maxx = 0;
        int key;
        unordered_map<int, pair<int, vector<int>>> umap;
        for (int & num: nums) {
            int max_count = 1;
            vector<int>* pattern;
            for (auto & it: umap) {
                if ((num % it.first == 0) && (it.second.first+1 > max_count)) {
                    max_count = it.second.first+1;
                    pattern = &it.second.second;
                }
            }

            vector<int> new_pattern;
            if (max_count != 1) {
                new_pattern = *pattern;
            }
            new_pattern.push_back(num);
            umap.insert(pair(num, pair(max_count, new_pattern)));

            if (maxx < max_count) {
                maxx = max_count;
                key = num;
            }
        }
        return umap.at(key).second;
    }
};
