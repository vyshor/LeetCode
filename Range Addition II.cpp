class Solution {
public:
    int maxCount(int m, int n, vector<vector<int>>& ops) {
        int minn_x = m-1, minn_y = n-1;
        for (auto& op: ops) {
            int a = op[0]-1, b = op[1]-1;
            minn_x = min(minn_x, a);
            minn_y = min(minn_y, b);
        }
        return (minn_x+1) * (minn_y+1);
    }
};
