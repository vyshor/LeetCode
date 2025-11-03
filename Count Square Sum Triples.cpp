class Solution {
public:
    int countTriples(int n) {
        unordered_set<int> sqs;
        vector<int> arr;
        for (int i = 1; i <= n; i++) {
            arr.push_back(i*i);
            sqs.insert(i*i);
        }
        int m = arr.size();
        int count = 0;
        for (int i = 0; i < m; i++) {
            for (int j = i; j < m; j++) {
                if (sqs.contains(arr[i] + arr[j])) {
                    count += 1 + (i != j);
                }
            }
        }
        return count;
    }
};
