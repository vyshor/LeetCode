class Solution {
public:
    int findLeastNumOfUniqueInts(vector<int>& arr, int k) {
        unordered_map<uint32_t, uint16_t> counter;
        for (auto & num: arr) {
            if (counter.find(num) == counter.end()) {
                counter.insert(make_pair(num, 1));
            } else {
                counter.at(num)++;
            }
        }

        vector<uint16_t> counts;
        int n = counter.size();
        counts.reserve(n);
        for (auto & iter: counter) {
            counts.push_back(iter.second);
        }
        sort(counts.begin(), counts.end());
        for (int i = 0; i < n; i++) {
            if (k < counts[i]) {
                return n-i;
            } else {
                k -= counts[i];
            }
        }
        return 0;
    }
};
