class Solution {
public:
    bool isNStraightHand(vector<int>& hand, int groupSize) {
        sort(hand.begin(), hand.end());
        unordered_map<int, int> counter;
        for (int& num: hand) {
            counter[num]++;
        }

        for (int& num: hand) {
            if (counter[num] > 0) {
                for (int i = num; i < num+groupSize; i++) {
                    if (--counter[i] < 0) return false;
                }
            }
        }
        return true;
    }
};
