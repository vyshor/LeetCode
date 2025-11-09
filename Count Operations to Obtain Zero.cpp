class Solution {
public:
    int countOperations(int num1, int num2) {
        if (num1 < num2) {
            swap(num1, num2);
        }
        int count = 0;
        while (num1 != 0 && num2 != 0) {
            // cout << num1 << " " << num2 << endl;
            num1 -= num2;
            count++;
            if (num1 < num2) {
                swap(num1, num2);
            }
        }
        return count;
    }
};
