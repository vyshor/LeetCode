class Solution {
public:
    int add(int i, int j, int& k) {
        i += j;
        if (i < 0) i += k;
        return i % k;
    }
    bool checkSubarraySum(vector<int>& nums, int k) {
        int n = nums.size();
        if (n == 1) return false;
        if (n == 2) return add(nums[0], nums[1], k) == 0;

        vector<int> prefixes(n, 0);
        vector<int> suffixes(n+1, 0);
        int total = 0;
        for (int i = 0; i < n; i++) {
            total = add(total, nums[i], k);
            prefixes[i] = total;
        }

        int t = 0;
        for (int i = n-1; i >= 0; i--) {
            t = add(t, nums[i], k);
            suffixes[i] = t;
        }

        unordered_set<int> seen{0};
        for (int i = 2; i <= n; i++) {
            int finding = add(total, -suffixes[i], k);
            if (seen.contains(finding)) return true;
            seen.insert(prefixes[i-2]);
        }
        return false;
    }
};

