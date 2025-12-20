bool MeetingComp(const vector<int>& a, const vector<int>& b) {
    return a[2] < b[2];
}

class Solution {
public:
    vector<int> findAllPeople(int n, vector<vector<int>>& meetings, int firstPerson) {
        vector<int> parents(n+1);
        vector<int> secrets(n+1);
        std::iota(parents.begin(), parents.end(), 0);
        secrets[0] = 1;
        secrets[firstPerson] = 1;

        function<int(int)> find;
        find = [&] (int i) -> int {
            if (parents[i] == i) return i;
            int new_parent = find(parents[i]);
            parents[i] = new_parent;
            return new_parent;
        };

        auto uni = [&] (int i, int j) {
            int parent_i = find(i);
            int parent_j = find(j);
            if (parent_i == parent_j) return;
            parents[parent_j] = parent_i;
            secrets[parent_i] |= secrets[parent_j];
        };

        std::sort(meetings.begin(), meetings.end(), MeetingComp);

        unordered_set<int> changed_nodes;
        int timestamp = 0;
        for (auto& meeting: meetings) {
            int i = meeting[0];
            int j = meeting[1];
            int ts = meeting[2];

            // std::cout << "Ts: " << ts << '\n';

            if (ts != timestamp) {
                // End of previous round
                for (int node: changed_nodes) {
                    secrets[node] |= secrets[find(node)];
                }
                for (int node: changed_nodes) {
                    parents[node] = node;
                }
                unordered_set<int> new_nodes;
                changed_nodes.swap(new_nodes);
                timestamp = ts;
            }

            uni(i, j);
            changed_nodes.insert(i);
            changed_nodes.insert(j);
        }

        for (int node: changed_nodes) {
            secrets[node] |= secrets[find(node)];
        }

        vector<int> ans;
        ans.reserve(n);
        for (int i{0}; i < n+1; ++i) {
            if (secrets[i]) {
                ans.push_back(i);
            }
        }
        return ans;
    }
};


class Solution {
public:
    vector<int> findAllPeople(int n, vector<vector<int>>& meetings, int firstPerson) {
        std::sort(meetings.begin(), meetings.end(),
            [](vector<int> const &a, vector<int> const &b) {
            return a.at(2) < b.at(2);
        });

        set<int> known({0, firstPerson});
        int prev_t = 0;
        unordered_map<int, vector<int>> dp;
        for (auto & meeting : meetings) {
            int x = meeting.at(0);
            int y = meeting.at(1);
            int t = meeting.at(2);

            if (t != prev_t) {
                dp.clear();
                prev_t = t;
            }

            if (!known.contains(x) && !known.contains(y)) {
                if (!dp.contains(x)) {
                    vector<int> v{y};
                    dp.insert(make_pair(x, v));
                } else
                    dp.at(x).push_back(y);

                if (!dp.contains(y)) {
                    vector<int> v{x};
                    dp.insert(make_pair(y, v));
                } else
                    dp.at(y).push_back(x);
            } else {
                vector<int> q{x, y};
                int i = 0;
                while (i < q.size()) {
                    int person = q.at(i);
                    known.insert(person);

                    if (dp.contains(person)) {
                        for (auto & other_person: dp.at(person)) {
                            if (dp.contains(other_person)) {
                                q.push_back(other_person);
                            }
                        }
                        dp.erase(person);
                    }
                    i++;
                }
            }
        }
        vector<int> ans(known.begin(), known.end());
        return ans;
    }
};
