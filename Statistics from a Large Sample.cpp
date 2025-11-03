class Solution {
public:
    vector<double> sampleStats(vector<int>& count) {
        constexpr int n = 256;
        int minn = n, maxx = 0;
        double summ = 0.;
        int64_t total_count = 0;
        int max_count = 0, mode_val = 0;;

        for (int i = 0; i < n; i++) {
            if (count[i] > 0) {
                minn = min(minn, i);
                maxx = max(maxx, i);
                if (count[i] > max_count) {
                    max_count = count[i];
                    mode_val = i;
                }
                total_count += count[i];
                summ += static_cast<double>(count[i]) * static_cast<double>(i);
            }
        }
        int odd_median = (total_count & 1);
        int median_count = (total_count+1) / 2;
        double median;
        int nxt_median = 0;
        for (int i = 0; i < n; i++) {
            if (nxt_median && count[i] > 0) {
                median += i;
                median /= 2;
                break;
            }

            if (count[i] > 0) {
                median_count -= count[i];
                if (odd_median) {
                    if (median_count <= 0) {
                        median = i;
                        break;
                    }
                } else {
                    if (median_count < 0) {
                        median = i;
                        break;
                    } else if (median_count == 0) {
                        median = i;
                        nxt_median = 1;
                    }
                }
            }
        }

        return {
            static_cast<double>(minn),
            static_cast<double>(maxx),
            summ / total_count,
            median,
            static_cast<double>(mode_val)
            };
    }
};
