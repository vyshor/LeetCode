class Solution {
public:
    vector<long long> sumOfThree(long long num) {
        if ((num % 3) != 0) return {};
        long long v = num / 3;
        return {v-1, v, v+1};
    }
};

