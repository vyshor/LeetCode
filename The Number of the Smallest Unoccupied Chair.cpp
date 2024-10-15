class Solution {
public:
    int smallestChair(vector<vector<int>>& times, int targetFriend) {
        int n = 0;
        vector<int> q;
        vector<vector<int>> t, chairs;
        for (int i = 0; i < times.size(); i++) {
            t.push_back({times[i][0], times[i][1], i});
        }

        sort(t.begin(), t.end());
        for (auto& arr: t) {
            while (chairs.size() >  0 && -chairs[0][0] <= arr[0]) {
                pop_heap(chairs.begin(), chairs.end());
                auto seat = chairs.back();
                chairs.pop_back();
                q.push_back(-seat[1]);
                push_heap(q.begin(), q.end());
            }

            int seat_num = n;
            if (q.size() > 0) {
                pop_heap(q.begin(), q.end());
                seat_num = -q.back();
                q.pop_back();
            } else {
                n++;
            }

            if (arr[2] == targetFriend) return seat_num;

            chairs.push_back({-arr[1], seat_num});
            push_heap(chairs.begin(), chairs.end());
        }
        return 0;
    }
};
