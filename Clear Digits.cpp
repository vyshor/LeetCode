class Solution {
public:
    string clearDigits(string s) {
        int n = s.size();
        std::vector<int> stack;
        int i = 0;
        for (char c: s) {
            if (isdigit(c) && stack.size() > 0) {
                s[stack.back()] = '!';
                s[i] = '!';
                stack.pop_back();
            } else if (!isdigit(c)) {
                stack.push_back(i);
            }
            i++;
        }
        // std::cout << s << std::endl;
        std::stringstream ss;
        for (char c: s) {
            if (c != '!') ss << c;
        }
        return ss.str();
    }
};