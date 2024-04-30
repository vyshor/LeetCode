class Solution {
public:
    long long wonderfulSubstrings(string word) {
        unordered_map<int16_t, int> counter;
        counter[0] = 1;
        int16_t current = 0;
        int64_t count = 0;
        for (char& c: word) {
            int16_t shift = 1 << (int) (c - 'a');
            current ^= shift;

            if (counter.contains(current)) {
                count += counter[current]++;
            } else {
                counter[current]++;
            }

            for (int i = 0; i < 10; i++) {
                int16_t new_mask = current ^ (1 << i);
                if (counter.contains(new_mask)) count += counter[new_mask];
            }
        }
        return count;
    }
};
