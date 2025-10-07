class Solution {
public:
    uint64_t total_points = 0;
    vector<int> match;
    vector<int> rect_summ;
    vector<vector<int>> rect_pos;
    mt19937 rng;
    uniform_int_distribution<int> gen; // uniform, unbiased

    Solution(vector<vector<int>>& rects) {
        rect_pos = std::move(rects);
        vector<int> rect_match;
        for (auto& pos: rect_pos) {
            int rect_points = (pos[2]+1-pos[0])*(pos[3]+1-pos[1]);
            // cout << rect_points << endl;
            total_points += rect_points;
            rect_match.push_back(rect_points);
        }
        // cout << total_points << endl;
        match = vector<int> (total_points, 0);
        int summ = 0;
        int j = 0;
        for (int rcount: rect_match) {
            rect_summ.push_back(summ);
            for (int i = summ; i < summ+rcount; i++) {
                match[i] = j;
            }
            summ += rcount;
            j++;
        }
        gen = uniform_int_distribution<int> (0, total_points-1);
    }

    vector<int> pick() {
        int idx = gen(rng);
        int rect_idx = match[idx];
        int offset = idx - rect_summ[rect_idx];
        vector<int>& rect = rect_pos[rect_idx];
        int row = rect[2]+1 - rect[0];
        int col_idx = offset / row;
        int row_idx = offset % row;
        return {rect[0] + row_idx, rect[1] + col_idx};
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(rects);
 * vector<int> param_1 = obj->pick();
 */
