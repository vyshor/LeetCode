class Solution {
public:
    int numOfUnplacedFruits(vector<int>& fruits, vector<int>& baskets) {
        int unplaced = 0;
        size_t n = baskets.size();
        for (int fruit: fruits) {
            bool placed = false;
            for (size_t i = 0; i < n; i++) {
                if (baskets[i] >= fruit) {
                    baskets[i] = 0;
                    placed = true;
                    break;
                }
            }
            if (!placed) {
                unplaced++;
            }
        }
        return unplaced;
    }
};