class Solution {
public:
    vector<int> countMentions(int numberOfUsers, vector<vector<string>>& events) {
        int n{numberOfUsers};
        vector<int> online(n, 1);
        vector<int> mentions(n, 0);
        const string msg{"MESSAGE"};
        const string msg_all{"ALL"};
        const string msg_here{"HERE"};

        vector<std::pair<int, int>> status;
        vector<std::pair<int, int>> messages;

        for (auto& event: events) {
            int timestamp = std::atoi(event[1].c_str());
            if (event[0] == msg) {
                if (event[2] == msg_all) {
                    messages.emplace_back(timestamp, -1);
                } else if (event[2] == msg_here) {
                    messages.emplace_back(timestamp, -2);
                } else {
                    int idx{0};
                    int strlen = event[2].size();
                    for (int i{1}; i < strlen; ++i) {
                        char ch = event[2][i];
                        if (ch == ' ') continue;
                        if (ch == 'd') {
                            idx = 0;
                        } else if (ch == 'i') {
                            ++mentions[idx];
                        } else {
                            idx *= 10;
                            idx += (ch - 48);
                        }
                    }
                    ++mentions[idx];
                }
            } else {
                int idx = std::atoi(event[2].c_str());
                status.emplace_back(timestamp, idx);
                status.emplace_back(timestamp+60, idx);
            }
        }

        std::sort(status.begin(), status.end());
        std::sort(messages.begin(), messages.end());
        int status_idx{0};
        int m = status.size();
        int all_count{0};


        for (auto [ts, target]: messages) {
            while (status_idx < m && status[status_idx].first <= ts) {
                online[status[status_idx].second] ^= 1;
                ++status_idx;
            }

            if (target == -1) {
                ++all_count;
            } else if (target == -2) {
                for (int i{0}; i < n; ++i) {
                    mentions[i] += online[i];
                }
            }
        }
        for (int i{0}; i < n; ++i) {
            mentions[i] += all_count;
        }
        return mentions;
    }
};
