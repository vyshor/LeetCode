class Solution {
public:
    vector<string> validateCoupons(vector<string>& code, vector<string>& businessLine, vector<bool>& isActive) {
        unordered_map<string, int> mapping = {
            {"electronics", 0},
            {"grocery", 1},
            {"pharmacy", 2},
            {"restaurant", 3}
        };

        vector<pair<int, string_view>> order;
        int n = code.size();
        for (int i = 0; i < n; i++) {
            if (!isActive[i] || code[i].size() == 0) continue;
            bool valid = true;
            for (char ch: code[i]) {
                if (!std::isalnum(ch) && ch != '_') {
                    valid = false;
                    break;
                }
            }
            if (!valid) continue;

            if (!mapping.contains(businessLine[i])) continue;

            order.emplace_back(mapping[businessLine[i]], code[i]);
        }
        sort(order.begin(), order.end());
        vector<string> ans;
        for (auto& [_, c]: order) {
            ans.push_back(string(c));
        }
        return ans;
    }
};
