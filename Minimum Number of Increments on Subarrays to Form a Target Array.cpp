class Solution {
public:
    int minNumberOperations(vector<int>& target) {
        vector<int> stack;
        int count = 0;
        for (int height: target) {
            while (stack.size() > 0 && height < stack.back()) {
                int prev_height = stack.back();
                stack.pop_back();
                int diff = prev_height - height;
                if (stack.size() > 0) diff = min(diff, prev_height-stack.back());
                count += diff;
            }
            if (stack.size() == 0 || stack.back() != height) {
                stack.push_back(height);
            }
        }
        return count+stack.back();
    }
};
