class Solution {
public:
    bool checkTwoChessboards(string coordinate1, string coordinate2) {
        int x0 = coordinate1[0] - 97, y0 = coordinate1[1] - 49;
        int x1 = coordinate2[0] - 97, y1 = coordinate2[1] - 49;
        return ((x0 & 1) ^ (y0 & 1)) == ((x1 & 1) ^ (y1 & 1));
    }
};
