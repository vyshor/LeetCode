int sum(vector<int>& v) {
    int total = 0;
    for (int &i: v) total += i;
    return total;
}

class Solution {
public:
    int countStudents(vector<int>& students, vector<int>& sandwiches) {
        int n = sandwiches.size();
        int n1 = sum(students), n2 = sum(sandwiches);
        if (n1 == n2) return 0;

        int what = 0;
        if (n1-n2>0) what = 1;
        int count, other_count;
        if (what == 0) {
            count = n-n2;
            other_count = n1;
        } else {
            count=n2;
            other_count = n-n1;
        }

        for (int i=0; i<n; i++) {
            if (sandwiches[i]==what) {
                if (count > 0) count--;
                else return n-i;
            } else {
                if (other_count > 0) other_count--;
                else return n-i;
            }
        }
        return 0;
    }
};
