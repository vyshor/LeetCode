class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        int i = 0;
        int j = nums.size() - 1;
        vector<int> arr;
        arr.reserve(nums.size());
        int sq_i = nums.at(i)*nums.at(i);;
        int sq_j = nums.at(j)*nums.at(j);;

        while (i < j) {
            if (sq_i > sq_j) {
                arr.push_back(sq_i);
                i++;
                sq_i = nums.at(i)*nums.at(i);
            } else {
                arr.push_back(sq_j);
                j--;
                sq_j = nums.at(j)*nums.at(j);
            }
        }

        arr.push_back(sq_i);
        i = 0;
        j = arr.size() - 1;
        while (i < j) {
            swap(arr.at(i++), arr.at(j--));
        }
        return arr;
    }
};
