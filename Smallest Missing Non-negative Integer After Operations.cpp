class Solution {
public:
    int findSmallestInteger(vector<int>& nums, int value) {
        vector<int> counter(value, 0);
        for (int num: nums) {
            if (num < 0) {
                int divsor = -(num / value)+1;
                num += divsor * value;
            }
            int remainder = num % value;
            counter[remainder]++;
        }

        int minn = counter[0];
        int idx = 0;
        for (int i = 0; i < value; i++) {
            // cout << "i=" << i << " " << counter[i] << endl;
            if (counter[i] < minn) {
                minn = counter[i];
                idx = i;
            }
        }
        return minn*value+idx;
    }
};
