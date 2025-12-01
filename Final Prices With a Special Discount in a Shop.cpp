class Solution {
public:
    vector<int> finalPrices(vector<int>& prices) {
        int n = prices.size();
        vector<pair<int, int>> stack;
        for (int i{0}; i < n; ++i) {
            while (stack.size() > 0 && prices[i] <= stack.back().first) {
                prices[stack.back().second] -= prices[i];
                stack.pop_back();
            }
            stack.emplace_back(prices[i], i);
        }
        return prices;
    }
};
