class Solution {
public:
    int mostBooked(int n, vector<vector<int>>& meetings) {
        int negative_shift = -100;
        vector<int> uses(n, 0);
        priority_queue<int, vector<int>, greater<int>> available;
        priority_queue<pair<int64_t, int64_t>, vector<pair<int64_t, int64_t>>, greater<pair<int64_t, int64_t>>> t;
        queue<pair<int, int>> q;

        for(int i=0; i<n;i++) {
            available.push(i);
        }

        for (auto & meeting: meetings) {
            t.push(make_pair(meeting.at(0), meeting.at(1)));
        }

        while (t.size() > 0) {
            auto p = std::move(t.top());
            t.pop();
            if (p.second > 0) {
                q.push(p);
            } else {
                available.push(p.second-negative_shift);
            }

            while (available.size() > 0 && q.size() > 0) {
                auto waiting_p = q.front();
                q.pop();
                uint32_t duration = waiting_p.second - waiting_p.first;
                int room = available.top();
                available.pop();
                uses.at(room)++;
                t.push(make_pair(p.first+duration, negative_shift+room));
            }
        }

        int maxx_count = uses.at(0);
        int j = 0;
        for (int i = 0;i<n;i++) {
            if (uses.at(i) > maxx_count) {
                j = i;
                maxx_count = uses.at(i);
            }
        }
        return j;
    }
};
