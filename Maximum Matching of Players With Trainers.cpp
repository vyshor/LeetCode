class Solution {
public:
    int matchPlayersAndTrainers(vector<int>& players, vector<int>& trainers) {
        sort(players.begin(), players.end());
        sort(trainers.begin(), trainers.end());

        size_t n = players.size(), m = trainers.size();
        size_t pidx = 0, tidx = 0;
        int count = 0;
        while (pidx < n) {
            while (tidx < m && players[pidx] > trainers[tidx]) tidx++;

            if (tidx < m && players[pidx] <= trainers[tidx]) {
                tidx++;
                count++;
            }
            pidx++;
        }
        return count;
    }
};
