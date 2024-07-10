class Solution {
public:
    int minOperations(vector<string>& logs) {
        int count = 0;
        for (string& log: logs) {
            if (log == "../") {
                if (--count < 0) count = 0;
            } else if (log != "./") {
                count++;
            }
        }
        return count;
    }
};
