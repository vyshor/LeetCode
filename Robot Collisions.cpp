class Solution {
public:
    vector<int> survivedRobotsHealths(vector<int>& positions, vector<int>& healths, string directions) {
        vector<vector<int>> arr;
        int n = positions.size();
        arr.reserve(n);
        for (int i = 0; i < n; i++) {
            arr.push_back({positions[i], i, healths[i], int(directions[i] == 'R')});
        }

        sort(arr.begin(), arr.end());
        vector<pair<int, int>> stack;
        vector<int> ans(n, 0);
        for (int i = 0; i < n; i++) {
            auto j = arr[i][1], h = arr[i][2], is_right = arr[i][3];
            if (is_right) {
                stack.emplace_back(j, h);
            } else {
                while (!stack.empty()) {
                    if (stack.back().second == h) {
                        h = 0;
                        stack.pop_back();
                        break;
                    } else if (stack.back().second > h) {
                        h = 0;
                        stack.back().second--;
                        break;
                    } else {
                        stack.pop_back();
                        h -= 1;
                    }
                }

                if (h) {
                    ans[j] = h;
                }
            }
        }

        for (auto [j, h]: stack) {
            ans[j] = h;
        }

        vector<int> t_ans;
        for (int h: ans) {
            if (h) t_ans.push_back(h);
        }
        return t_ans;
    }
};

