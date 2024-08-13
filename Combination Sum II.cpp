class Solution {
public:
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        map<int, int> counter;
        vector<int> row;
        for (int num: candidates) {
            counter[num]++;
            if (counter[num] == 1) row.push_back(num);
        }

        int total = target;
        int n = row.size();
        vector<vector<int>> ans;
        vector<int> curr;

        function<void(int)> explore;
        explore = [&explore, &counter, &row, &total, &n, &ans, &curr] (int i) {
            if (i == n) return;

            int num = row[i];
            for (int j = 0; j < counter[num]+1; j++) {
                total -= num * j;
                if (total < 0) {
                    total += num * j;
                    continue;
                }

                for (int k = 0; k < j; k++) {
                    curr.push_back(num);
                }

                if (total == 0) {
                    auto dup = curr;
                    ans.push_back(dup);
                    total += num * j;

                    for (int k = 0; k < j; k++) curr.pop_back();
                    continue;
                }

                explore(i+1);
                for (int k = 0; k < j; k++) curr.pop_back();

                total += num*j;
            }
        };
        explore(0);
        return ans;
    }
};
