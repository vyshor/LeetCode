class Solution {
public:
    bool isPowerOfTwo(int n) {
        return (n != 0) && (n > 0) && ((n & (n-1)) == 0);
    }
};

//class Solution {
//public:
//    bool isPowerOfTwo(int n) {
//        uint8_t single_one = 0;
//        while (n > 0) {
//            if (n & single_one == 1) return false;
//            single_one |= n & 1;
//            n >>= 1;
//        }
//        return single_one == 1;
//    }
//};
