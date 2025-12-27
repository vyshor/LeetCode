class Solution {
public:
    int mostBooked(int n, vector<vector<int>>& meetings) {
        vector<int> rooms_count(n, 0);
        vector<int> available(n);

        std::iota(available.begin(), available.end(), 0);
        std::make_heap(available.begin(), available.end(), std::greater<>{});

        vector<tuple<int64_t, int, int, int64_t>> q; // Ts, is_start, room, duration
        deque<pair<int64_t, int64_t>> pending_meetings;

        for (auto& meeting: meetings) {
            q.emplace_back(meeting[0], 1, -1, meeting[1]-meeting[0]);
        }
        std::make_heap(q.begin(), q.end(), std::greater<>{});

        while (q.size() > 0) {
            std::pop_heap(q.begin(), q.end(), std::greater<>{});
            auto [ts, is_start, room, duration] = q.back();
            q.pop_back();

            if (is_start) {
                // Meeting start
                pending_meetings.emplace_back(ts, duration);
            } else {
                // Meeting end
                available.push_back(room);
                std::push_heap(available.begin(), available.end(), std::greater<>{});

            }

            while (pending_meetings.size() > 0 && available.size() > 0) {
                std::pop_heap(available.begin(), available.end(), std::greater<>{});
                int room = available.back();
                available.pop_back();

                ++rooms_count[room];

                auto [_, meeting_duration] = pending_meetings.front();
                pending_meetings.pop_front();

                q.emplace_back(ts+meeting_duration, 0, room, -1);
                std::push_heap(q.begin(), q.end(), std::greater<>{});
            }
        }

        int maxx{-1};
        int idx{0};
        for (int i{0}; i < n; ++i) {
            if (rooms_count[i] > maxx) {
                maxx = rooms_count[i];
                idx = i;
            }
        }

        return idx;
    }
};


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
