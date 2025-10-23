class Solution {
public:
    bool hasSameDigits(string s) {
        int n = s.size();
        vector<int> arr(n, 0);
        for (int i = 0; i < n; i++) {
            arr[i] = s[i]-48;
        }

        for (int i = n; i > 2; i--) {
            for (int j = 0; j < i-1; j++) {
                arr[j] = (arr[j] + arr[j+1]) % 10;
            }
        }
        return arr[0] == arr[1];
    }
};
