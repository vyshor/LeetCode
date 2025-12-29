class Solution {
public:
    std::map<pair<char, char>, vector<char>> vmapping;
    vector<vector<char>> pyramid;
    int target;

    int recur(int i, int j) {
        if (i == target) return 1;

        if (j == pyramid[i].size() - 1) return recur(i+1, 0);
        pair<char, char> key = std::make_pair(pyramid[i][j], pyramid[i][j+1]);
        if (vmapping.contains(key)) {
            for (char nxt_char: vmapping[key]) {
                pyramid[i+1].push_back(nxt_char);
                int result = recur(i, j+1);
                if (result) return result;
                pyramid[i+1].pop_back();
            }
        }
        return 0;
    }

    bool pyramidTransition(string bottom, vector<string>& allowed) {
        target = bottom.size() - 1;
        pyramid = vector<vector<char>>(bottom.size(), vector<char>(0));
        pyramid[0] = vector<char>(bottom.begin(), bottom.end());

        for (string& combo: allowed) {
            vmapping[{combo[0], combo[1]}].push_back(combo[2]);
        }

        return recur(0, 0);
    }
};
