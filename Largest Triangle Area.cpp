class Solution {
public:
    double calculate(vector<int>& pointA, vector<int>& pointB, vector<int>& pointC) {
        return 0.5 * abs(pointA[0]*(pointB[1]-pointC[1]) + pointB[0]*(pointC[1]-pointA[1]) + pointC[0]*(pointA[1]-pointB[1]));
    };

    double largestTriangleArea(vector<vector<int>>& points) {
        int n = points.size();
        double maxx = 0.;
        for (int i = 0; i < n; i++) {
            for (int j = i+1; j < n; j++) {
                for (int k = j+1; k < n; k++) {
                    maxx = max(maxx, calculate(points[i], points[j], points[k]));
                }
            }
        }
        return maxx;
    }
};