class Solution {
public:
    int maxBottlesDrunk(int numBottles, int numExchange) {
        int count = numBottles;
        while (numBottles >= numExchange) {
            count++;
            numBottles += 1 - numExchange;
            numExchange++;
        }
        return count;
    }
};