class Solution {
public:
    int minOperations(vector<int>& nums, int k) {
        std::vector<int64_t> arr;
        for (int num: nums) {
            if (num < k) arr.push_back((int64_t) -num);
        }

        make_heap(arr.begin(), arr.end());
        int n = arr.size();
        int count = 0;
        while (n > 1) {
            pop_heap(arr.begin(), arr.end());
            int64_t minn = arr.back();
            arr.pop_back();
            pop_heap(arr.begin(), arr.end());
            int64_t minn2 = arr.back();
            arr.pop_back();
            int64_t x = (minn << 1) + minn2;
            if (x > -k) {
                arr.push_back(x);
                push_heap(arr.begin(), arr.end());
                n--;
            } else {
                n -= 2;
            }
            count++;
        }
        return count + n;
    }
};