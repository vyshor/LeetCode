class Solution {
public:
    int closestToTarget(vector<int>& arr, int target) {
        set<int> seen;
        int minn = INT_MAX;

        for (int val: arr) {
            set<int> new_seen{val};
            minn = min(minn, abs(target-val));
            // cout << "Val:" << val << " Min: " << minn << endl;

            for (int seen_val: seen) {
                new_seen.insert(seen_val & val);
                minn = min(minn, abs(target-(seen_val & val)));
                // cout << "Seen_val:" << seen_val  <<  " Val:" << val << " Min: " << minn << endl;
            }

            seen.swap(new_seen);
        }
        return minn;
    }
};
