class Solution {
public:
    int openLock(vector<string>& deadends, string target) {
        deque<pair<string, int>> q;
        unordered_set<string> stuck(deadends.begin(), deadends.end());
        if (target == "0000") return 0;
        if (stuck.contains("0000")) return -1;
        unordered_set<string> visited{"0000"};
        q.emplace_back("0000", 0);

        while (q.size() > 0) {

            auto [num_str, steps] = q.front();
            q.pop_front();
            steps++;

            for (int i = 0; i < 4; i++) {
                for (int j = -1; j < 2; j += 2) {
                    int val = ((int) num_str[i] - (int) '0' + j + 10) % 10;
                    string new_num_str = num_str.substr(0, i) + (char) (val + (int) '0') + num_str.substr(i+1);
                    if (visited.contains(new_num_str) || stuck.contains(new_num_str)) continue;

                    if (new_num_str == target) return steps;

                    q.push_back(make_pair(new_num_str, steps));
                    visited.insert(new_num_str);
                }
            }
        }
        return -1;
    }
};
