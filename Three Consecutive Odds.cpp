class Solution {
public:
    bool threeConsecutiveOdds(vector<int>& arr) {
        int count = 0;
        for (int num: arr) {
            count = (count + num % 2) * (num % 2);
            if (count == 3) return true;
        }
        return false;
    }
};
