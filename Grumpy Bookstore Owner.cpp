class Solution {
public:
    int maxSatisfied(vector<int>& customers, vector<int>& grumpy, int minutes) {
        int n = customers.size();
        vector<int> arr(n, 0);
        int total = 0, summ = 0;
        for (int i = 0; i < n; i++) {
            total += !grumpy[i] * customers[i];
            arr[i] = customers[i] * grumpy[i];
            summ += arr[i] * (i < minutes-1);
        }

        int maxx = summ;
        int left =0, right =minutes-1;
        while (right < n) {
            summ += arr[right];
            maxx = max(maxx, summ);
            summ -= arr[left];
            right++;
            left++;
        }
        return total + maxx;
    }
};
