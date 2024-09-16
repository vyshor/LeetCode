class Solution {
public:
    int convert(string s) {
        return stoi(s.substr(0, 2)) * 60 + stoi(s.substr(3));
    }
    int findMinDifference(vector<string>& timePoints) {
        vector<int> arr;
        for (string& tp: timePoints) {
            arr.push_back(convert(tp));
        }

        sort(arr.begin(), arr.end());
        int minn = arr[0] + 24 * 60 - arr.back();
        for (int i = 0; i < arr.size()-1; i++) {
            minn = min(minn, arr[i+1]-arr[i]);
        }
        return minn;
    }
};
