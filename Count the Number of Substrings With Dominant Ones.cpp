class Solution {
public:
    int numberOfSubstrings(string s) {
        int n = s.size();
        int count = 0;
        int zeroes = 0;
        for (int i = 0; i < n; ++i) {
            zeroes += s[i] == '0';
        }
        int maxx_zeroes = min(static_cast<int>(sqrt(n) + 1.), zeroes);
        for (int i = 0; i < maxx_zeroes+1; ++i) {
            int left = 0, right = 0;
            int z = 0;
            int ones_required = i*i;
            deque<int> prev_idx;
            // cout << "i=" << i << endl;

            while (right < n) {
                if (s[right] == '0') {
                    prev_idx.push_back(right);
                    ++z;
                }

                if (z < i) {
                    ++right;
                    continue;
                }

                while (z > i) {
                    left = prev_idx.front()+1;
                    prev_idx.pop_front();
                    --z;
                }

                int ones = right-left+1-z;
                int excess_ones = ones - ones_required;
                if (excess_ones >= 0) {
                    // cout << "Left=" << left << ", Right=" << right << endl;
                    // cout << "Excess=" << excess_ones << endl;
                    if (i > 0) {
                        count += min(excess_ones, prev_idx.front()-left)+1;
                    } else {
                        count += excess_ones;
                    }
                    // cout << "Count=" << count << endl;
                }

                ++right;
            }
        }
        return count;
    }
};
