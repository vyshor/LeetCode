class Solution {
public:
    int minimumBoxes(vector<int>& apple, vector<int>& capacity) {
        int summ{0};
        for (int count: apple) {
            summ += count;
        }
        sort(capacity.begin(), capacity.end());
        int n = capacity.size();
        if (summ == 0) return 0;
        for (int i = n-1; i >= 0; --i) {
            summ -= capacity[i];
            if (summ <= 0) return n-i;
        }
        return n;
    }
};
