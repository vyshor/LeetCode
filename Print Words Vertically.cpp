class Solution {
public:
    vector<string> printVertically(string s) {
        vector<stringstream> arr;
        int count = 0;
        int str_count = 0;
        for (char ch: s) {
            if (ch == ' ') {
                count = 0;
                str_count++;
                continue;
            } else {
                if (arr.size() < (count+1)) {
                    arr.emplace_back();

                }
                if (arr[count].str().size() < str_count) {
                    arr[count] << string(str_count - arr[count].str().size(), ' ');
                }
                arr[count] << ch;
                count++;
            }
        }
        vector<string> ans;
        for (auto& ss: arr) {
            ans.push_back(ss.str());
        }
        return ans;
    }
};
