class Solution {
public:
    vector<long long> findXSum(vector<int>& nums, int k, int x) {
        int n = nums.size();

        // Lowest freq, and lowest val
        set<pair<int64_t, int64_t>, less<>> topN;

        // Highest freq, and highest val
        set<pair<int64_t, int64_t>, greater<>> bot;

        vector<long long> ans;
        unordered_map<int64_t, int64_t> counter;
        for (int i = 0; i < k; i++) {
            counter[nums[i]]++;
        }

        vector<pair<int64_t, int64_t>> arr;
        for (auto [val, freq]: counter) {
            arr.emplace_back(freq, val);
        }
        sort(arr.begin(), arr.end());
        int m = arr.size();
        int64_t summ = 0;
        for (int i = m-1; i >= 0; i--) {
            if (topN.size() < x) {
                summ += arr[i].first * arr[i].second;
                topN.insert(std::move(arr[i]));
            } else {
                bot.insert(std::move(arr[i]));
            }
        }
        ans.push_back(summ);
        int right = k;
        while (right < n) {
            int old_val = nums[right-k];
            int new_val = nums[right];

            if (old_val != new_val) {
                // Remove first
                pair<int64_t, int64_t> old_pair = {counter[old_val], old_val};
                if (topN.contains(old_pair)) {
                    topN.erase(old_pair);
                    topN.emplace(counter[old_val]-1, old_val);

                    summ -= old_val;
                } else {
                    bot.erase(old_pair);
                    bot.emplace(counter[old_val]-1, old_val);
                }

                pair<int64_t, int64_t> new_pair = {counter[new_val], new_val};
                if (topN.contains(new_pair)) {
                    topN.erase(new_pair);
                    topN.emplace(counter[new_val]+1, new_val);
                    summ += new_val;
                } else {
                    bot.erase(new_pair);
                    bot.emplace(counter[new_val]+1, new_val);
                }

                counter[old_val]--;
                counter[new_val]++;

                // We do swapping for those in bot that are valid
                while (bot.size() > 0 && *bot.begin() > *topN.begin()) {
                    auto down = *topN.begin();
                    auto up = *bot.begin();

                    // cout << "Down= " << down.first << " " << down.second << endl;
                    // cout << "Up= " << up.first << " " << up.second << endl;

                    summ += up.first*up.second - down.first*down.second;
                    topN.erase(down);
                    topN.insert(up);

                    bot.erase(up);
                    bot.insert(down);
                }

                while (topN.size() < x && bot.size() > 0) {
                    auto up = *bot.begin();
                    bot.erase(up);
                    topN.insert(up);

                    summ += up.first*up.second;
                }
            }

            ans.push_back(summ);
            right++;
        }

        return ans;
    }
};