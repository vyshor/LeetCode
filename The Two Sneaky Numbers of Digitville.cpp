class Solution {
public:
    vector<int> getSneakyNumbers(vector<int>& nums) {
        bitset<100> seen;
        vector<int> ans;
        for (int num: nums) {
            if (seen[num]) ans.push_back(num);
            seen.set(num);
        }
        return ans;
    }
};

class Solution {
public:
    vector<int> getSneakyNumbers(vector<int>& nums) {
        int n = nums.size();
        vector<int> seen(n, 0);
        vector<int> ans;
        for (int num: nums) {
            if (seen[num]) ans.push_back(num);
            seen[num]= 1;
        }
        return ans;
    }
};
