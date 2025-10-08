class Solution {
public:
    vector<int> successfulPairs(vector<int>& spells, vector<int>& potions, long long success) {
        sort(potions.begin(), potions.end());
        vector<int> ans;
        int n = potions.size();
        for (int64_t spell: spells) {
            int64_t min_potion = (success / spell) + ((success % spell) != 0);
            if (min_potion > INT_MAX) {
                ans.push_back(0);
                continue;
            }
            int mpotion = min_potion;
            auto ptr = lower_bound(potions.begin(), potions.end(), mpotion);
            int idx = ptr-potions.begin();
            ans.push_back(n-idx);
        }
        return ans;
    }
};
