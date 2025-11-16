class Solution {
public:
    vector<string> buildArray(vector<int>& target, int n) {
        vector<string> ans;
        ans.reserve(n*2);
        int m = target.size();
        int last_target = target.back();
        vector<int> seen(n+1);
        for (int v: target) {
            seen[v] = 1;
        }
        for (int i = 1; i < last_target+1; ++i) {
            ans.emplace_back("Push"s);
            if (!seen[i]) ans.emplace_back("Pop"s);
        }
        return ans;
    }
};