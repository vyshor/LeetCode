class Solution {
public:
    int maxProfit(vector<int>& prices) {
        vector<int> state(4, INT_MIN);
        int n = prices.size();
        for (int i = 0; i < n; i++) {
            if (state[2] != INT_MIN) state[3] = max(state[3], state[2]+prices[i]);
            if (state[1] != INT_MIN) state[2] = max(state[2], state[1]-prices[i]);
            if (state[0] != INT_MIN) state[1] = max(state[1], state[0]+prices[i]);
            state[0] = max(state[0], -prices[i]);
        }
        state.push_back(0);
        return *max_element(state.begin(), state.end());
    }
};
