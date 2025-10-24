class Solution {
public:
    vector<int> decimalRepresentation(int n) {
        vector<int> ans;
        int64_t i = 1;
        while (n != 0) {
            int dec = n % 10;
            if ((dec) != 0) {
                ans.push_back(dec*i);
            }
            n /= 10;
            i *= 10;
        }
        std::reverse(ans.begin(), ans.end());
        return ans;
    }
};
