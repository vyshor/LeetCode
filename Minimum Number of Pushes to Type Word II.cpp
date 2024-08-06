class Solution {
public:
    int minimumPushes(string word) {
        map<char, int> counter;
        for (char c: word) counter[c]++;
        vector<int> q;
        for (auto [_, v]: counter) q.push_back(-v);
        sort(q.begin(), q.end());
        int pushes = 0, num_pad = 0, rotation = 1;
        for (int count : q) {
            pushes += -count * rotation;
            num_pad++;
            if (num_pad == 8) {
                rotation++;
                num_pad = 0;
            }
        }
        return pushes;
    }
};
