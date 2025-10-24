class Solution {
public:
    vector<int> recoverOrder(vector<int>& order, vector<int>& friends) {
        int n = order.size();
        vector<int> isfriend(n+1, 0);
        for (int f: friends) {
            isfriend[f] = 1;
        }
        vector<int> ans;
        for (int id: order) {
            if (isfriend[id]) ans.push_back(id);
        }
        return ans;
    }
};
