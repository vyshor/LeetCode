class Solution {
public:
    vector<int> frequencySort(vector<int>& nums) {
        map<int, int> counter;
        for (int num: nums) {
            counter[num]++;
        }

        struct compare
        {
            map<int, int>* counter_;
            compare(map<int, int>* counter) : counter_(counter) {}

            inline bool operator() (int i, int j)
            {
                if ((*counter_)[i] == (*counter_)[j]) return i > j;
                return (*counter_)[i] < (*counter_)[j];
            }
        };

        sort(nums.begin(), nums.end(), compare(&counter));
        return nums;
    }
};
