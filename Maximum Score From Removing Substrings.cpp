class Solution {
public:
    int maximumGain(string s, int x, int y) {
        int score = 0;
        auto find_ab = [&score] (vector<char> s, char a, char b, int delta) -> vector<char> {
            int n = s.size();
            vector<char> stack;
            for (int i = 0; i < n; i++) {
                if (s[i] == b && !stack.empty() && stack.back() == a) {
                    score += delta;
                    stack.pop_back();
                } else {
                    stack.push_back(s[i]);
                }
            }
            return stack;
        };

        vector<char> stack(s.begin(), s.end());
        if (x > y) {
            find_ab(find_ab(stack, 'a', 'b', x), 'b', 'a', y);
        } else {
            find_ab(find_ab(stack, 'b', 'a', y), 'a', 'b', x);
        }
        return score;
    }
};
