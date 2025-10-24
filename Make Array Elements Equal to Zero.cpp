class Solution {
public:
    int countValidSelections(vector<int>& nums) {
        int summ = 0;
        for (int num: nums) summ += num;
        int psumm = 0;
        int count = 0;
        for (int num: nums) {
            psumm += num;
            if (num == 0) {
                int rsumm = summ - psumm;
                count += ((psumm == rsumm+1) || (psumm == rsumm)) + ((psumm+1 == rsumm) || (psumm == rsumm));
            }
        }
        return count;
    }
};
