class Solution {
public:
    int minLength(string s) {
        vector<char> stack;
        for (char c: s) {
            if (c == 'D' && stack.size() > 0 && stack.back() == 'C') stack.pop_back();
            else if (c == 'B' && stack.size() > 0 && stack.back() == 'A') stack.pop_back();
            else stack.push_back(c);
        }
        return stack.size();
    }
};
