class Solution {
public:
    string removeKdigits(string num, int k) {
        int n = num.size();
        if (k == n) return "0";

        vector<char> stack;
        for (char & c: num) {
            while (stack.size() > 0 && stack.back() > c && k > 0) {
                stack.pop_back();
                k--;
            }

            stack.push_back(c);
        }

        while (k > 0) {
            stack.pop_back();
            k--;
        }

        bool non_zero = false;
        stringstream ss;
        for (char & c: stack) {
            if (c == '0' && !non_zero) {
                continue;
            }

            non_zero = true;
            ss << c;
        }

        string ans = ss.str();
        if (ans.size() == 0) return "0";
        return ans;
    }
};
