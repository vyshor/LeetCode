class Solution {
public:
    bool isPossibleDivide(vector<int>& nums, int k) {
        unordered_map<int, int> counter;
        for (int& num: nums) {
            if (!counter.contains(num))
                counter.insert(make_pair(num, 1));
            else
                counter[num]++;
        }

        while (counter.size() > 0) {
            int smallest = -1;
            for (auto& kvpair: counter) {
                if (smallest == -1)
                    smallest = kvpair.first;
                else
                    smallest = min(smallest, kvpair.first);
            }

            for (int num = smallest; num < smallest+k; num++) {
                if (!counter.contains(num)) return false;
                counter[num]--;
                if (counter[num] == 0) counter.erase(num);
            }
        }
        return true;
    }
};
