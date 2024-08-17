class Solution {
public:
    int smallestDistancePair(vector<int>& nums, int k) {
        map<int, int> counter;
        vector<int> keys;
        for (int num: nums) {
            if (counter[num]++ == 0) {
                keys.push_back(num);
            }
        }
        sort(keys.begin(), keys.end());
        int n = keys.size();

        for (int i = 0; i < n; i++) {
            if (counter[keys[i]] > 1) k -= (counter[keys[i]] * counter[keys[i]]-1) / 2;
        }

        if (k <= 1) return 0;

        auto check = [&keys, &counter, &n, &k] (int window) -> bool {
            int left = 0, limit = keys[left]+window, i=left+1, count=0;
            while (i < n && keys[i] <= limit) {
                count += counter[keys[i++]];
            }
            int total = counter[keys[left]] * count;

            while (left < n-1) {
                if (k <= total) return true;
                left++;
                count -= counter[keys[left]];
                limit = keys[left] + window;
                while (i < n && keys[i] <= limit) {
                    count += counter[keys[i++]];
                }
                total += counter[keys[left]] * count;
            }
            return k <= total;
        };

        int minn = 1, maxx = keys.back() - keys.front();
        while (minn < maxx) {
            int mid = (minn+maxx) / 2;
            bool left_side = check(mid);
            if (left_side) maxx = mid;
            else minn = mid+1;
        }
        return minn;
    }
};
