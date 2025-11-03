class Solution {
public:
    int minCost(string colors, vector<int>& neededTime) {
        int n = neededTime.size();
        int count = 1;
        int summ = neededTime[0];
        int maxxTime = neededTime[0];
        int prev_color = colors[0];
        int total = 0;
        for (int i = 1; i < n; ++i) {
            if (colors[i] == prev_color) {
                ++count;
                summ += neededTime[i];
                maxxTime = max(maxxTime, neededTime[i]);
            } else {
                // Clear previous
                if (count > 1) {
                    total += summ - maxxTime;
                }
                count = 1;
                summ = neededTime[i];
                maxxTime = neededTime[i];
                prev_color = colors[i];
            }
        }

        if (count > 1) {
            total += summ - maxxTime;
        }
        return total;
    }
};
