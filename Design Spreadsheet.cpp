class Spreadsheet {
public:
    vector<vector<int>> sheet;
    Spreadsheet(int rows) {
        sheet = vector<vector<int>>(26, vector<int>(rows, 0));
    }

    int readVal(string val) {
        if (val[0] >= 65) {
            auto idx = getIndex(val);
            return sheet[idx.first][idx.second];
        } else {
            return stoi(val);
        }
    }

    pair<int, int> getIndex(string cell) {
        auto ptr = cell.data();
        string row_str(ptr+1);
        int row = stoi(row_str);
        return {(*ptr-65), row-1};
    }

    void setCell(string cell, int value) {
        auto idx = getIndex(cell);
        // cout << idx.first << " " << idx.second << endl;
        sheet[idx.first][idx.second] = value;
    }

    void resetCell(string cell) {
        auto idx = getIndex(cell);
        sheet[idx.first][idx.second] = 0;
    }

    int getValue(string formula) {
        const char* ptr = formula.c_str();
        ptr++;
        stringstream ss;
        while (*ptr != '+') {
            ss << *ptr;
            ptr++;
        }

        ptr++;
        string first_val = ss.str();
        string second_val(ptr);
        return readVal(first_val) + readVal(second_val);
    }
};

/**
 * Your Spreadsheet object will be instantiated and called as such:
 * Spreadsheet* obj = new Spreadsheet(rows);
 * obj->setCell(cell,value);
 * obj->resetCell(cell);
 * int param_3 = obj->getValue(formula);
 */