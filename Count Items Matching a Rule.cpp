class Solution {
public:
    int countMatches(vector<vector<string>>& items, string ruleKey, string ruleValue) {
        unordered_map<string, int> mapping = {
            {"type", 0},
            {"color", 1},
            {"name", 2},
        };
        int count = 0;
        int type_idx = mapping[ruleKey];
        for (auto& item: items) {
            count += (item[type_idx] == ruleValue);
        }
        return count;
    }
};
