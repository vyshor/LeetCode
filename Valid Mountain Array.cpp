class Solution {
public:
    bool validMountainArray(vector<int>& arr) {
        int n = arr.size();
        if (n < 3) return false;

        int i = 0, j = n-1;
        while (i < j && arr[i] < arr[i+1]) i++;
        while (i < j && arr[j-1] > arr[j]) j--;

        return i == j && j != n-1 && i != 0;
    }
};

