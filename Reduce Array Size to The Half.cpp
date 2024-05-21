class Solution {
public:
    int minSetSize(vector<int>& arr) {
        int n = arr.size();
        int m = n / 2 + (n % 2);
        unordered_map<int, int> counter;
        for (int& num: arr) {
            if (!counter.contains(num)) {
                counter[num] = 1;
            } else {
                counter[num]++;
            }
        }

        vector<int> vals;
        vals.reserve(counter.size());
        for (auto [_, v]: counter) {
            vals.push_back(-v);
        }
        sort(vals.begin(), vals.end());

        for (int i = 0; i < vals.size(); i++) {
            n += vals[i];
            if (n <= m) return i+1;
        }
        return 0;
    }
};
