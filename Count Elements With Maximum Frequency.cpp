class Solution {
public:
    int maxFrequencyElements(vector<int>& nums) {
        unordered_map<int, int> counter;
        int maxx = 0;
        int max_count = 0;
        for (auto & num: nums) {
            int val;
            if (counter.find(num) == counter.end()) {
                counter.insert(make_pair(num, 1));
                val = 1;
            } else {
                val = ++counter.at(num);
            }

            if (val > maxx) {
                maxx = val;
                max_count = 1;
            } else if (val == maxx) {
                max_count++;
            }
        }
        return maxx * max_count;
    }
};
