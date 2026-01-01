class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        std::reverse(digits.begin(), digits.end());
        int carry{1};
        int n = digits.size();
        for (int i{0}; i < n; ++i) {
            int digit = digits[i] + carry;
            carry = digit / 10;
            digit %= 10;
            digits[i] = digit;
        }
        if (carry > 0) {
            digits.push_back(carry);
        }
        std::reverse(digits.begin(), digits.end());
        return digits;
    }
};
