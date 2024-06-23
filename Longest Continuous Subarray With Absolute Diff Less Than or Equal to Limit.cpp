class Solution {
public:
    int longestSubarray(vector<int>& nums, int limit) {
        int n = nums.size();
        unordered_map<int, int> counter;
        vector<int> minn, maxx;
        int left =0, right = 0, count = 0;
        while (right < n) {
            int num = nums[right];
            counter[num] += 1;

            minn.push_back(-num);
            push_heap(minn.begin(), minn.end());
            maxx.push_back(num);
            push_heap(maxx.begin(), maxx.end());

            while (maxx[0]+minn[0] > limit) {
                num = nums[left];
                counter[num]--;
                while (counter[maxx[0]] == 0) {
                    pop_heap(maxx.begin(), maxx.end());
                    maxx.pop_back();
                }

                while (counter[-minn[0]] == 0) {
                    pop_heap(minn.begin(), minn.end());
                    minn.pop_back();
                }
                left++;
            }

            if (maxx[0]+minn[0] <= limit) count = max(count, right-left+1);

            right++;
        }
        return count;
    }
};
