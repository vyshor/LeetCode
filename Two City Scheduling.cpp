class Solution {
public:
    int twoCitySchedCost(vector<vector<int>>& costs) {
        int n = costs.size();
        int min_total = 0;
        vector<int> extra_costs;
        for (auto& cost: costs) {
            min_total += cost[0];
            extra_costs.push_back(cost[1]-cost[0]);
        }
        sort(extra_costs.begin(), extra_costs.end());
        for (int i = 0; i < n/2; i++) {
            min_total += extra_costs[i];
        }
        return min_total;
    }
};
