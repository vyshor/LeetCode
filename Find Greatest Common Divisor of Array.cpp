class Solution {
public:
    int gcd(int a, int b) {
        if (a == 0) return b;
        return gcd(b % a, a);
    }
    int findGCD(vector<int>& nums) {
        return gcd(*ranges::min_element(nums), *ranges::max_element(nums));
    }
};

