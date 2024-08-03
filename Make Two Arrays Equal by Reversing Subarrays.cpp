class Solution {
public:
    bool canBeEqual(vector<int>& target, vector<int>& arr) {
        map<int, int> counter;
        for (int num: target) {
            counter[num]++;
        }

        for (int num: arr) {
            if (--counter[num] < 0)  return false;
        }
        return true;
    }
};
