class Solution {
public:

    int answer_count = 0;
    int cols = 0;
    int forwards = 0;
    int backwards = 0;

    int forward(int col_num, int row_num) {
        return (1 << (col_num + row_num));
    };

    int backward(int col_num, int row_num, int n) {
        col_num = n-1-col_num;
        return (1 << (col_num + row_num));
    };

    void pickRow(int row_num, int n) {
        cout << "Row num: " << row_num << endl;
        for (int i = 0; i < n; i++) {
            // Check if able to put down
            int row = 1 << row_num;
            int col = 1 << i;
            int ffor = forward(i, row_num);
            int bbac = backward(i, row_num, n);

            // cout << "Col:" << (col & cols) << endl;
            // cout << "For:" << (ffor & forwards) << endl;
            // cout << "Bac:" << (bbac & backwards) << endl;

            if (((col & cols) | (ffor & forwards) | (bbac & backwards)) > 0) {
                continue;
            }

            // Able put down
            cols |= col;
            forwards |= ffor;
            backwards |= bbac;

            // cout << "Placed at " << row_num << "," << i << endl;

            if (row_num == n-1) {
                answer_count++;
            } else {
                pickRow(row_num+1, n);
            }

            // cout << "Removed from " << row_num << "," << i << endl;

            cols ^= col;
            forwards ^= ffor;
            backwards ^= bbac;
        }
    }

    int totalNQueens(int n) {
        pickRow(0, n);
        return answer_count;
    }
};
