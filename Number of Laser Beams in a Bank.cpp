class Solution {
public:
    int numberOfBeams(vector<string>& bank) {
        int prev = 0;
        int lasers = 0;
        for (string& s: bank) {
            int count = 0;
            for (char ch: s) {
                count += (ch == '1');
            }
            if (count > 0) {
                lasers += prev*count;
                prev = count;
            }
        }
        return lasers;
    }
};
