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
