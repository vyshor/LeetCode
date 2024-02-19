class Solution {
public:
    int furthestBuilding(vector<int>& heights, int bricks, int ladders) {
        int n = heights.size();
        vector<pair<int, int>> diffs;
        diffs.push_back(make_pair(0, 0));

        int h = heights.at(0);
        for (int i=1; i<n; i++) {
            if (heights.at(i) > h)
                diffs.push_back(make_pair(heights.at(i)-h, i));
            else
                diffs.back().second = i;
            h = heights.at(i);
        }

        int m = diffs.size();
        if (ladders >= m-1) return n-1;

        priority_queue<int, vector<int>, greater<int>> q;
        int pos = diffs.at(ladders).second;
        for (int i=1; i<=ladders; i++)
            q.push(diffs.at(i).first);

        int i = ladders+1;
        while (i < m) {
            q.push(diffs.at(i).first);
            bricks -= q.top();
            if (bricks < 0) return pos;
            q.pop();
            pos = diffs.at(i).second;
            i++;
        }
        return pos;
    }
};
