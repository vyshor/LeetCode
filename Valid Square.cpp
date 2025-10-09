class Solution {
public:
    bool validSquare(vector<int>& p1, vector<int>& p2, vector<int>& p3, vector<int>& p4) {
        // Find leftmost bottom point, and rightmost top point
        vector<pair<int, int>> pts{
            {p1[0], p1[1]},
            {p2[0], p2[1]},
            {p3[0], p3[1]},
            {p4[0], p4[1]}
        };
        sort(pts.begin(), pts.end());
        auto& leftpt = pts[0];
        auto& rightpt = pts[3];

        auto& spt = pts[1];
        auto& tpt = pts[2];

        if (leftpt == spt) return false;

        int vsquare = ((tpt.first + (spt.first - leftpt.first)) == rightpt.first);
        vsquare &= ((tpt.second + (spt.second - leftpt.second)) == rightpt.second);
        vsquare &= ((spt.first + (tpt.first - leftpt.first)) == rightpt.first);
        vsquare &= ((spt.second + (tpt.second - leftpt.second)) == rightpt.second);
        int dist = ((spt.first-leftpt.first)*(spt.first-leftpt.first)+(spt.second-leftpt.second)*(spt.second-leftpt.second));
        int dist2 = ((tpt.first-leftpt.first)*(tpt.first-leftpt.first)+(tpt.second-leftpt.second)*(tpt.second-leftpt.second));
        vsquare &= (dist == dist2);
        int grad = (spt.second-leftpt.second)*(tpt.second-leftpt.second);
        int grad2 = (tpt.first-leftpt.first)*(spt.first-leftpt.first);
        // cout << grad << " " << grad2 << " " << (grad == -grad2) << endl;
        vsquare &= (grad == -grad2);
        return vsquare;
    }
};
