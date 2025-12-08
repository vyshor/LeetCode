class Solution {
public:
    // void print(vector<int>& v) {
    //     std::cout << "arr=";
    //     for (int i: v) {
    //         std::cout << i << ' ';
    //     }
    //     std::cout << '\n';
    // }

    int countPartitions(vector<int>& nums, int k) {
        int n = nums.size();
        int mod = 1e9 + 7;
        unordered_map<int, int> counter;
        set<int, std::greater<int>> maxx;
        set<int> minn;
        vector<int> diff(n+2, 0);
        diff[0] = 1;
        diff[1] = -1;
        int left{0}, right{0};
        int count{0};
        while (left < n) {

            // print(diff);

            count += diff[left];
            count %= mod;

            if (left == right) {
                int right_num = nums[right];
                ++counter[right_num];
                maxx.insert(right_num);
                minn.insert(right_num);
                ++right;
            }

            while (right < n) {
                int right_num = nums[right];
                if (max(*maxx.begin(), right_num) - min(*minn.begin(), right_num) > k) {
                    break;
                }

                ++counter[right_num];
                maxx.insert(right_num);
                minn.insert(right_num);
                ++right;
            }

            diff[left+1] = (diff[left+1] + count) % mod;
            diff[right+1] = (diff[right+1] - count + mod) % mod;

            int num = nums[left];
            if (--counter[num] == 0) {
                maxx.erase(num);
                minn.erase(num);
            }
            ++left;
        }

        // print(diff);
        return (count + diff[n]) % mod;
    }
};
