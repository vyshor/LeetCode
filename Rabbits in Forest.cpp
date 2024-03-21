class Solution {
public:
    int numRabbits(vector<int>& answers) {
        unordered_map<int, int> counter;
        int total = 0;
        for (int& num: answers) {
            if (!counter.contains(num)) {
                counter.insert(make_pair(num, 1));
            } else {
                counter.at(num)++;
            }

            if (counter.at(num) % (num+1) == 1 || num == 0) total += num+1;
        }

        return total;
    }
};
