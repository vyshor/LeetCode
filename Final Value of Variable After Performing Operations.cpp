class Solution {
public:
    int finalValueAfterOperations(vector<string>& operations) {
        int count = 0;
        for (string& op: operations) {
            count += 1 - (2* (op[1] == '-'));
        }
        return count;
    }
};
