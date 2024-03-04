class Solution {
public:
    int maxNumberOfFamilies(int n, vector<vector<int>>& reservedSeats) {
        auto getCount = [&] (uint8_t state) -> int {
            uint8_t left = (state & 0b0011) == 0b0011;
            uint8_t right = (state & 0b1100) == 0b1100;
            uint8_t mid = (state & 0b0110) == 0b0110;

            if (left && right) {
                return 2;
            } else {
                if (left || right || mid) {
                    return 1;
                } else{
                    return 0;
                }
            }
        };

        unordered_map<int, uint8_t> states;
        int count = n*2;
        for (auto & reservedSeat: reservedSeats) {
            int row = reservedSeat.at(0);
            int seat = reservedSeat.at(1);

            uint8_t prev_state = 0b1111;
            if (states.contains(row)) {
                prev_state = states.at(row);
            } else {
                states.insert(make_pair(row, prev_state));
            }

            int old_count = getCount(prev_state);
            if (old_count == 0) {
                continue;
            }

            uint8_t new_state = prev_state;
            switch (seat) {
                case 2:
                case 3:
                new_state &= 0b0111;
                break;

                case 4:
                case 5:
                new_state &= 0b1011;
                break;

                case 6:
                case 7:
                new_state &= 0b1101;
                break;

                case 8:
                case 9:
                new_state &= 0b1110;
                break;

                default:
                continue;
            }

            if (new_state == prev_state) continue;

            int new_count = getCount(new_state);
            count -= old_count - new_count;
            states.at(row) = new_state;
        }
        return count;
    }
};
