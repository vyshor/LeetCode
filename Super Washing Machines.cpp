class Solution {
public:
    int findMinMoves(vector<int>& machines) {
        int total = 0;
        int n = machines.size();
        for (int count: machines) {
            total += count;
        }
        if (total % n != 0) return -1;
        int required = total / n;
        // cout << "Required=" << required << endl;
        int carry = 0;

        vector<int> output(n, 0);
        for (int i = 0; i < n; i++) {
            int carry = machines[i]-required+carry;
            if (carry < 0) {
                output[i+1] += -carry;
            }
            if (carry > 0) {
                output[i] += carry;
            }
        }

        int maxx = 0;
        for (int i = 0; i < n; i++) {
            maxx = max(maxx, output[i]);
        }
        return maxx;
    }
};
