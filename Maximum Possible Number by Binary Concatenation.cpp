string to_bit(int i) {
    stringstream ss;
    while (i > 0) {
        ss << (i & 1);
        i >>= 1;
    }
    string s = ss.str();
    std::reverse(s.begin(), s.end());
    return s;
}

bool compare(const string& a, const string& b) {
    string c{a+b};
    string c2{b+a};
    return c > c2;
}

class Solution {
public:
    int maxGoodNumber(vector<int>& nums) {
        int n = nums.size();
        vector<string> nstr;
        for (int num: nums) {
            nstr.push_back(to_bit(num));
        }
        sort(nstr.begin(), nstr.end(), compare);

        int ans{0};
        for (const string& numstr: nstr) {
            // cout << numstr << endl;
            for (char ch: numstr) {
                ans <<= 1;
                ans |= ch - 48;
            }
        }
        return ans;
    }
};