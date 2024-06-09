class Solution {
public:
    int add(int i, int j, int& k) {
        i += j;
        while (i < 0) i += k;
        return i % k;
    }

    int subarraysDivByK(vector<int>& nums, int k) {
        int n = nums.size();

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

        int count = 0;
        unordered_map<int, int> seen;
        seen[0] = 1;
        for (int i = 1; i <= n; i++) {
            int finding = add(total, -suffixes[i], k);
            count += seen[finding];
            seen[prefixes[i-1]]++;
        }
        return count;
    }
};


