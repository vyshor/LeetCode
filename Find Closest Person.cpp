class Solution {
public:
    int findClosest(int x, int y, int z) {
        int xz = abs(x-z), yz = abs(y-z);
        return (1 + int(xz > yz))*int((xz != yz));
    }
};