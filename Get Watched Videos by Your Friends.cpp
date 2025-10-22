class Solution {
public:
    vector<string> watchedVideosByFriends(vector<vector<string>>& watchedVideos, vector<vector<int>>& friends, int id, int level) {
        int n = watchedVideos.size();
        deque<pair<int, int>> q = {{id, 0}};
        vector<int> visited(n, 0);
        vector<int> level_friends;
        while (q.size() > 0) {
            auto [i, lvl] = q.front();
            q.pop_front();
            if (visited[i]) continue;
            visited[i] = 1;

            if (lvl == level) {
                level_friends.push_back(i);
                continue;
            }

            for (int second_friend: friends[i]) {
                if (!visited[second_friend]) q.emplace_back(second_friend, lvl+1);
            }
        }

        vector<pair<int, string>> ans;
        unordered_map<string, int> counter;
        for (int i: level_friends) {
            for (string& video: watchedVideos[i]) {
                counter[video]++;
            }
        }

        for (auto& [video, count]: counter) {
            ans.emplace_back(count, std::move(video));
        }

        sort(ans.begin(), ans.end());
        vector<string> videos;
        for (auto& [_, video]: ans) {
            videos.push_back(std::move(video));
        }
        return videos;
    }
};
