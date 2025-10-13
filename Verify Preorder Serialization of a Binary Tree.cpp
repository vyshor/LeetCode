class Solution {
public:
    bool isValidSerialization(string preorder) {
        int count = 1;
        int n = preorder.size();
        int ptr = 0;
        int v = 0;
        while (ptr < n) {
            char ch = preorder[ptr];
            if (ch == '#') {
                count--;
                ptr++;
                // cout << "count: " << count << endl;
                if (count < 0) return false;
                continue;
            } else if (ch == ',') {
                if (v) count++; // Consume one, give back two
                v = 0;
                // cout << "count: " << count << endl;
            } else {
                if (count <= 0) return false;
                v |= 1;
            }
            ptr++;
        }
        if (v) count++;
        return count == 0;
    }
};
