class Solution {
public:
    string minRemoveToMakeValid(string s) {
        vector<int> stack;
        set<int> removed;
        for (int i = 0; i < s.size(); i++) {
            switch (s[i]) {
                case ')':
                    if (stack.size() == 0) removed.insert(i);
                    else stack.pop_back();
                    break;
                case '(':
                    stack.push_back(i);
            }
        }

        for (int& i: stack) removed.insert(i);
        stringstream ss;
        for (int i = 0; i < s.size(); i++) {
            if (!removed.contains(i)) ss << s[i];
        }
        return ss.str();
    }
};
