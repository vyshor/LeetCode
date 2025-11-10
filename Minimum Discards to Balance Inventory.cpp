class Solution {
public:
    int minArrivalsToDiscard(vector<int>& arrivals, int w, int m) {
        unordered_map<int, int> counter;
        int n = arrivals.size();
        vector<int> discarded(n, 0);
        int count = 0;
        for (int i = 0; i < w; ++i) {
            int arrival = arrivals[i];
            if (counter[arrival]+1 > m) {
                ++count;
                discarded[i] = 1;
            } else {
                ++counter[arrival];
            }
        }

        for (int i = w; i < n; ++i) {
            if (!discarded[i-w]) {
                int old_arrival = arrivals[i-w];
                --counter[old_arrival];
            }
            int arrival = arrivals[i];
            if (counter[arrival]+1 > m) {
                ++count;
                discarded[i] = 1;
            } else {
                ++counter[arrival];
            }
        }
        return count;
    }
};
