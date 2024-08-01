class Solution {
public:
    int countSeniors(vector<string>& details) {
        int count = 0;
        for (string& detail: details) {
            string c{detail[11], detail[12]};
            count += int(stoi(c) > 60);
        }
        return count;
    }
};
