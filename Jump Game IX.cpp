class Solution {
public:
    vector<int> maxValue(vector<int>& nums) {
        int n = nums.size();
        vector<int> ans(n);
        ans[0] = nums[0];
        int maxx = nums[0];
        for (int i = 1; i < n; ++i) {
            int num = nums[i];
            maxx = max(maxx, num);
            ans[i] = maxx;
        }

        int minn = nums[n-1];
        maxx = ans[n-1];
        for (int i = n-2; i >= 0; i--) {
            if (ans[i] > minn) {
                ans[i] = max(ans[i], ans[i+1]);
            }
            minn = min(minn, nums[i]);
        }
        return ans;
    }
};


class Solution {
public:
    vector<int> maxValue(vector<int>& nums) {
        int n = nums.size();
        vector<int> parents(n);
        std::iota(parents.begin(), parents.end(), 0);

        function<int(int)> find;
        find = [&find, &parents] (int i) -> int{
            if (parents[i] == i) return i;
            int parent = find(parents[i]);
            parents[i] = parent;
            return parent;
        };

        auto uni = [&find, &parents] (int i, int j) {
            int parent_i = find(i);
            int parent_j = find(j);
            if (parent_i == parent_j) return;

            parents[parent_j] = parent_i;
        };

        vector<pair<int, int>> stack = {{nums[0], 0}};
        for (int i = 1; i < n; ++i) {
            int num = nums[i];
            auto& top_stack = stack.back();
            stack.pop_back();

            while (stack.size() > 0 && stack.back().first > num) {
                uni(i, stack.back().second);
                stack.pop_back();
            }

            if (num < top_stack.first) {
                uni(top_stack.second, i);
                stack.push_back(std::move(top_stack));
            } else {
                stack.push_back(std::move(top_stack));
                stack.emplace_back(nums[i], i);
            }
        }

        vector<int> ans(n);
        for (int i = 0; i < n; ++i) {
            ans[i] = nums[find(i)];
        }
        return ans;
    }
};
