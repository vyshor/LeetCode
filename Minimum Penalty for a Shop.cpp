class Solution {
public:
    int bestClosingTime(string customers) {
        int opened = 0, closed = 0, j = 0, n = customers.size();
        for (int i = 0; i < n; i++) {
            bool coming = customers[i] == 'Y';
            closed += coming;
            if (opened+coming < closed) {
                closed = opened+coming;
                j = i;
            }

            opened += !coming;
        }
        if (opened < closed) return n;
        return j;
    }
};
