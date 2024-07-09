class Solution {
public:
    double averageWaitingTime(vector<vector<int>>& customers) {
        int64_t t0 = 0, total = 0;
        for (auto customer: customers) {
            int a = customer[0], t = customer[1];
            total += t + (t0-a) * (t0 > a);
            t0 = a*(t0 <= a) + t0*(t0 > a) + t;
        }
        return static_cast<double>(total) / static_cast<double>(customers.size());
    }
};
