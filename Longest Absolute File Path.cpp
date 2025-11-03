class Solution {
public:
    int lengthLongestPath(string input) {
        vector<int> levels;
        int maxx = 0;
        int current_level = 0;
        int word_length = 0;
        int is_file = 0;
        for (char ch: input) {
            if (ch == '\n') {
                // Termination of previous line
                if (is_file) {
                    maxx = max(maxx, word_length+current_level);
                }

                if (levels.size() == current_level) levels.push_back(word_length);
                else {
                    levels[current_level] = word_length;
                }

                // Reset word
                current_level = 0;
                word_length = 0;
                is_file = 0;
            } else if (ch == '\t') {
                current_level++;
                word_length = levels[current_level-1];
            } else {
                if (ch == '.') is_file = 1;
                word_length++;
            }
        }
        if (is_file) maxx = max(maxx, word_length+current_level);
        return maxx;
    }
};
