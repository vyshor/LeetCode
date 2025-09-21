class Solution {
public:
    int totalFruit(vector<int>& fruits) {
        size_t n = fruits.size();
        unordered_map<int, int> counter;
        size_t left_ptr = 0;
        int maxx = 0;
        int count = 0;
        for (size_t i = 0; i < n; i++) {
            int fruit = fruits[i];
            counter[fruit]++;
            count++;

            while (counter.size() > 2) {
                int left_fruit = fruits[left_ptr];
                counter[left_fruit]--;
                if (counter[left_fruit] == 0) counter.erase(left_fruit);
                left_ptr++;
                count--;
            }
            maxx = max(count, maxx);
        }
        return maxx;
    }
};
