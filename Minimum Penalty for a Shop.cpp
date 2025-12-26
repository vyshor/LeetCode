class Solution {
public:
    int bestClosingTime(string customers) {
        int opened{0}, closed{0};
        int t{0};
        int i{0};
        for (char cust: customers) {
            if (cust == 'Y') {
                ++closed;
                if (opened + 1 < closed) {
                    t = i;
                    closed = opened+1;
                }
            } else {
                ++opened;
                if (opened-1 < closed) {
                    t = i;
                    closed = opened-1;
                }
            }
            ++i;
        }
        if (opened < closed) return customers.size();
        return t;
    }
};

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
