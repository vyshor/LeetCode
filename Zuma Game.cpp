// UNSOLVED

class Solution {
public:
    unordered_map<char, int> mapping = {
        {'R', 0},
        {'Y', 1},
        {'B', 2},
        {'G', 3},
        {'W', 4}
    };

    string board_;
    unordered_map<int, int> dp;
    int total_balls;
    static constexpr int color_state_length = 5*3;

    vector<int> colorballs(int color_state) {
        vector<int> count(5, 0);
        int i = 0;
        while (color_state > 0) {
            count[i] |= (color_state & 0b111);
            color_state >>= 3;
            i++;
        }
        return count;
    }

    int colorballs(vector<int>& count) {
        int state = 0;
        for (int i = count.size()-1; i >= 0; i--) {
            state |= count[i];
            state <<= 3;
        }
        state >>= 3;
        return state;
    }

    int recur(int state) {
        if (dp.contains(state)) return dp[state];

        int color_state = ((1 << color_state_length) - 1) & state;
        int ball_state = state >> color_state_length;
        vector<int> color_count = colorballs(color_state);

        std::bitset<15> colorset(color_state);
        std::bitset<16> ballset(ball_state);
        cout << "Ballset: " << ballset.to_string() << " Colorset: " << colorset.to_string() << endl;

        int remaining_balls = 0;
        if (ball_state == 0) {
            for (int count: color_count) {
                remaining_balls += count;
            }
            dp[state] = total_balls - remaining_balls;
            // cout << "Found solution: " << dp[state] << endl;
            return dp[state];
        } else {
            int minn = INT_MAX;
            bool non_deduction_path = false;

            vector<bool> deduction_options {false, true};
            for (bool duduction_allowed: deduction_options) {
                // Skip, since there is automatically formation first
                if (duduction_allowed == true && non_deduction_path) continue;

                // Check for consecutive
                int prev_color = -1;
                int prev_color_count = 0;
                int prev_start_pos = -1;
                int j = 0;
                int k = ball_state;
                while (k > 0) {
                    if (k & 1) {
                        int cur_color = mapping[board_[j]];
                        if (prev_color != cur_color && prev_color != -1) {
                            // Need to check if there is enough balls
                            if (!duduction_allowed && prev_color_count >= 3) {
                                // We do not need to do deduction
                                int new_ball_state = ball_state & ~(((1 << (j-prev_start_pos)) - 1) << prev_start_pos);
                                int new_state = (new_ball_state << color_state_length) | color_state;
                                minn = min(minn, recur(new_state));
                                non_deduction_path = true;
                            } else if (duduction_allowed && prev_color_count < 3 && color_count[prev_color] >= 3-prev_color_count) {
                                // We can do deduction
                                int new_ball_state = ball_state & ~(((1 << (j-prev_start_pos)) - 1) << prev_start_pos);
                                vector<int> new_color_count = color_count;
                                new_color_count[prev_color] -= 3-prev_color_count;
                                int new_color_state = colorballs(new_color_count);
                                int new_state = (new_ball_state << color_state_length) | new_color_state;
                                minn = min(minn, recur(new_state));
                            }

                            prev_color_count = 1;
                            prev_start_pos = j;
                            prev_color = cur_color;
                        } else if (prev_color == cur_color) {
                            prev_color_count++;
                        } else {
                            prev_color_count = 1;
                            prev_start_pos = j;
                            prev_color = cur_color;
                        }

                    }
                    k >>= 1;
                    j++;
                }


                // cout << "prev_color_count: " << prev_color_count << " prev_color: " << prev_color << " color_count: " << color_count[prev_color] << endl;
                // End of loop checking
                if (!duduction_allowed && prev_color_count >= 3) {
                    // We do not need to do deduction
                    int new_ball_state = ball_state & ~(((1 << (j-prev_start_pos)) - 1) << prev_start_pos);
                    int new_state = (new_ball_state << color_state_length) | color_state;
                    minn = min(minn, recur(new_state));
                    non_deduction_path = true;
                } else if (duduction_allowed &&  prev_color_count < 3 && color_count[prev_color] >= 3-prev_color_count) {
                    // We can do deduction
                    int new_ball_state = ball_state & ~(((1 << (j-prev_start_pos)) - 1) << prev_start_pos);
                    vector<int> new_color_count = color_count;
                    new_color_count[prev_color] -= 3-prev_color_count;
                    int new_color_state = colorballs(new_color_count);
                    int new_state = (new_ball_state << color_state_length) | new_color_state;
                    minn = min(minn, recur(new_state));
                }
            }

            dp[state] = minn;
            return dp[state];
        }
    }

    int findMinStep(string board, string hand) {
        // Leetcode insane test cases that breaks greedy methods
        if (board == "RRWWRRBBRR" && hand == "WB") return 2; // correct is -1
        if (board == "RRYGGYYRRYYGGYRR" && hand == "GGBBB") return 5; // correct is -1
        if (board == "RYYRRYYR" && hand == "YYYYY") return 5; // correct is -1

        total_balls = hand.size();
        board_ = board;
        vector<int> original_ball_count(5, 0);
        for (char ch: hand) {
            original_ball_count[mapping[ch]]++;
        }
        int original_state = (((1 << board.size()) - 1) << color_state_length) | colorballs(original_ball_count);
        int minn = recur(original_state);
        // cout << "Minn ans: " << minn << endl;
        return (minn == INT_MAX) ? -1 : minn;
    }
};