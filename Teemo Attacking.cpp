class Solution {
public:
    int findPoisonedDuration(vector<int>& timeSeries, int duration) {
        int start = 0, end = -1;
        int poison = 0;
        for (int attack: timeSeries) {
            if (end < attack) {
                poison += (end-start+1);
                start = -1;
            }

            if (start == -1) {
                start = attack;
            }
            end = attack+duration-1;
        }
        poison += end-start+1;
        return poison;
    }

};