class Solution {
public:
    vector<int> diff;
    int least_k;
    bool check(vector<int>& nums) {
        int summ = 0;
        for (int i = 0; i < nums.size(); i++) {
            summ += diff[i];

            if (nums[i] > summ) return false;
        }
        return true;
    }

    void update(vector<vector<int>>& queries, int k) {
        fill(diff.begin(), diff.end(), 0);
        for (int i = 0; i < k; i++) {
            auto& query = queries[i];
            int l = query[0], r = query[1], val = query[2];
            diff[l] += val;
            diff[r+1] -= val;
        }
    }

    void binary_search(int lower, int upper, vector<int>& nums, vector<vector<int>>& queries) {
        // cout << lower << " " << upper << endl;
        if (lower >= upper) {
            update(queries, lower);
            bool valid = check(nums);
            if (valid) {
                least_k = min(least_k, lower);
                // cout << "Least k " << least_k << endl;
            }
            return;
        }
        int mid = (lower+upper) / 2;
        update(queries, mid);
        bool valid = check(nums);
        if (valid) {
            least_k = min(least_k, mid);
            binary_search(lower, mid, nums, queries);
        } else {
            binary_search(mid+1, upper, nums, queries);
        }
    }

    int minZeroArray(vector<int>& nums, vector<vector<int>>& queries) {
        int n = nums.size();
        int m = queries.size();
        diff.resize(n+1, 0);
        least_k = m+1;

        if (check(nums)) return 0;
        binary_search(0, queries.size(), nums, queries);
        if (least_k == m+1) return -1;
        return least_k;
    }
};
