class Solution {
public:
    int countTriplets(vector<int>& arr) {
        vector<pair<int, int>> dp;
        int count = 0;
        for (int num: arr) {
            auto i = lower_bound(dp.begin(), dp.end(), make_pair(num, 0));
            int m = 0;
            for (auto j = dp.begin(); j != i; j++) {
                count += j->second;
                m++;
            }
            dp.insert(i, make_pair(num, m));
        }
        return count;
    }
    int numTeams(vector<int>& rating) {
        int count = countTriplets(rating);
        reverse(rating.begin(), rating.end());
        return count + countTriplets(rating);
    }
};
