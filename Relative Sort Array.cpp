class Solution {
public:
    vector<int> relativeSortArray(vector<int>& arr1, vector<int>& arr2) {
        unordered_map<int, int> counter;
        for (int& num: arr1) {
            counter[num]++;
        }

        vector<int> ans;
        ans.reserve(arr1.size());

        for (int& num: arr2) {
            int count = counter[num];
            for (int i = 0; i < count; i++) {
                ans.push_back(num);
            }
            counter.erase(num);
        }

        vector<int> remaining;
        for (auto& [num, count]: counter) {
            for (int i = 0; i < count; i++) {
                remaining.push_back(num);
            }
        }
        sort(remaining.begin(), remaining.end());
        ans.insert( ans.end(), remaining.begin(), remaining.end() );
        return ans;
    }
};
