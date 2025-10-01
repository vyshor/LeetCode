class Solution {
public:
    int numWaterBottles(int numBottles, int numExchange) {
        int count = numBottles;
        while (numBottles >= numExchange) {
            int mul = numBottles / numExchange;
            int val = mul * numExchange;
            count += mul;
            numBottles += mul - val ;
        }
        return count;
    }
};

class Solution {
public:
    int numWaterBottles(int numBottles, int numExchange) {
        int count = 0, remainder = 0;
        while (numBottles) {
            count += numBottles;
            numBottles += remainder;
            remainder = numBottles % numExchange;
            numBottles /= numExchange;
        }
        return count;
    }
};
