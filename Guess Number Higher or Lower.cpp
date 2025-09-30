/**
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * int guess(int num);
 */

class Solution {
public:
    int guessNumber(int n) {
        int lower = 1, upper = n;
        int result = 1;
        while (result != 0) {
            int mid = ((lower >> 1) + (upper >> 1)) + (((lower & 1) + (upper & 1)) >> 1);
            result = guess(mid);
            if (result == 0) return mid;
            if (result == 1) {
                lower = mid+1;
            } else {
                upper = mid;
            }
        }
        return -1;
    }
};