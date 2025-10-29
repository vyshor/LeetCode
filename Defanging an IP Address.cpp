class Solution {
public:
    string defangIPaddr(string address) {
        stringstream ss;
        for (char ch: address) {
            if (ch == '.') {
                ss << "[.]";
            } else{
                ss << ch;
            }
        }
        return ss.str();
    }
};