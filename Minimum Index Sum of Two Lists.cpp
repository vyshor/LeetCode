class Solution {
public:
    vector<string> findRestaurant(vector<string>& list1, vector<string>& list2) {
        unordered_map<string, int> counter;
        int n = list1.size();
        for (int i = 0; i < n; i++) {
            counter[list1[i]] = i;
        }
        n = list2.size();
        int minn = INT_MAX;
        vector<string> ans;
        for (int i = 0; i < n; i++) {
            if (counter.contains(list2[i])) {
                int summ = counter[list2[i]] + i;
                if (summ < minn) {
                    minn = summ;
                    ans = {list2[i]};
                } else if (summ == minn) {
                    ans.push_back(list2[i]);
                }
            }
        }
        return ans;
    }
};
