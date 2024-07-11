class Solution {
public:
    pair<vector<char>, int> accumulate(int i, int n, string& s) {
        vector<char> arr;
        while (1) {
            if (i >= n) {
                return make_pair(arr, i);
            }
            if (s[i] == ')') {
                reverse(arr.begin(), arr.end());
                return make_pair(arr, i+1);
            }

            if (s[i] == '(') {
                auto [arr2, j] = accumulate(i+1, n, s);
                arr.insert(arr.end(), arr2.begin(), arr2.end());
                i = j;
                continue;
            }

            arr.push_back(s[i]);
            i++;
        }
    }

    string reverseParentheses(string s) {
        auto [arr, _] = accumulate(0, s.size(), s);
        string ans(arr.begin(), arr.end());
        return ans;
    }
};
