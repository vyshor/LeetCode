class Solution {
public:
    vector<int> addToArrayForm(vector<int>& num, int k) {
        string s = std::to_string(k);
        std::reverse(s.begin(), s.end());
        std::reverse(num.begin(), num.end());

        int n = s.size();
        int carry = 0;
        for (int i = 0; i < n; i++) {
            int val = s[i]-48;
            val += carry;
            if (i < num.size()) {
                num[i] += val;
            } else {
                num.push_back(val);
            }
            carry = num[i] / 10;
            num[i] %= 10;
        }

        int i = n;
        while (carry) {
            if (i < num.size()) {
                num[i] += carry;
                carry = num[i] / 10;
                num[i] %= 10;
            } else {
                num.push_back(carry);
                carry = 0;
            }
            i++;
        }
        std::reverse(num.begin(), num.end());
        return num;
    }
};
