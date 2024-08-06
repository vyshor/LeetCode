class Solution {
public:
    string kthDistinct(vector<string>& arr, int k) {
        map<string, int> counter;
        for (string& s: arr) counter[s]++;
        for (string& s: arr) {
            if (counter[s] == 1) {
                if (--k == 0) return s;
            }
        }
        return "";
    }
};