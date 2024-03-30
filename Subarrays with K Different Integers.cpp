class Solution {
public:
    int subarraysWithKDistinct(vector<int>& nums, int k) {
        unordered_map<int, int> last_pos;
        int n = nums.size();
        int count = 0, left = 0, right = 0;
        deque<pair<int, int>> q;

        while (right < n) {
            int num = nums[right];
            last_pos[num] = right;
            q.push_back(make_pair(num, right));

            while (last_pos.size() > k || last_pos[q.front().first] != q.front().second) {
                auto p = q.front();
                q.pop_front();
                if (p.second == last_pos[p.first]) {
                    left = last_pos[p.first]+1;
                    last_pos.erase(p.first);
                }
            }

            if (last_pos.size() == k)
                count += q.front().second - left + 1;
            right++;
        }
        return count;
    }
};
