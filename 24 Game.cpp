class Solution {
public:
    vector<vector<pair<int, int>>> dp;
    vector<int> values;

    int count_bits(int i) {
        int count = 0;
        for (int j = 0; j < 4; j++) {
            count += (i & 1);
            i >>= 1;
        }
        return count;
    }

    vector<pair<int, int>> recur(int bitmask) {
        if (dp[bitmask].size() > 0) return dp[bitmask];

        int bit_count = count_bits(bitmask);
        if (bit_count == 1) {
            for (int i = 0; i < 4; i++) {
                if ((bitmask >> i) & 1) {
                    dp[bitmask] = {{values[i], 1}};
                    return dp[bitmask];
                }
            }
        }

        // cout << "Bitcount:" << bit_count << endl;

        // Do all combinations
        // Selecting only one and remaining
        vector<pair<int, int>> results;
        int mask = bitmask;
        for (int i = 0; i < 4; i++) {
            if ((mask >> i) & 1) {
                int opposite_mask = bitmask ^ (1 << i);
                vector<pair<int, int>> left_results = recur(1 << i);
                vector<pair<int, int>> right_results = recur(opposite_mask);

                for (auto [lefttop, leftbot]: left_results) {
                    for (auto [righttop, rightbot]: right_results) {
                        results.emplace_back(lefttop*rightbot+leftbot*righttop, leftbot*rightbot);
                        results.emplace_back(lefttop*rightbot-leftbot*righttop, leftbot*rightbot);
                        results.emplace_back(lefttop*righttop, leftbot*rightbot);
                        results.emplace_back(lefttop*rightbot, leftbot*righttop);

                        // Opposite order
                        results.emplace_back(lefttop*rightbot-leftbot*righttop, leftbot*rightbot);
                        results.emplace_back(leftbot*righttop, lefttop*rightbot);
                    }
                }
            }
        }

        // Special case handling, where it is 2 and 2
        vector<int> combinations = {0b0011, 0b0101, 0b1001};
        if (bit_count == 4) {
            for (int comb: combinations) {
                int opposite_mask = bitmask ^ comb;
                vector<pair<int, int>> left_results = recur(comb);
                vector<pair<int, int>> right_results = recur(opposite_mask);

                for (auto [lefttop, leftbot]: left_results) {
                    for (auto [righttop, rightbot]: right_results) {
                        results.emplace_back(lefttop*rightbot+leftbot*righttop, leftbot*rightbot);
                        results.emplace_back(lefttop*rightbot-leftbot*righttop, leftbot*rightbot);
                        results.emplace_back(lefttop*righttop, leftbot*rightbot);
                        results.emplace_back(lefttop*rightbot, leftbot*righttop);

                        // Opposite order
                        results.emplace_back(lefttop*rightbot-leftbot*righttop, leftbot*rightbot);
                        results.emplace_back(leftbot*righttop, lefttop*rightbot);
                    }
                }
            }
        }

        dp[bitmask] = std::move(results);
        return dp[bitmask];
    }

    bool judgePoint24(vector<int>& cards) {
        dp = vector<vector<pair<int, int>>>(16);
        values = std::move(cards);
        auto all_results = recur(0b1111);
        for (auto [top, bot]: all_results) {
            if (bot == 0) continue;
            // cout << "Top=" << top << " bot=" << bot << endl;
            if ((top % bot) == 0 && (top/bot) == 24) return true;
        }
        return false;
    }
};
