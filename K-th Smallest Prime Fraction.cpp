class Solution {
public:
    vector<int> kthSmallestPrimeFraction(vector<int>& arr, int k) {
        int n = arr.size();
        vector<pair<float, pair<int, int>>> q;
        for (int i = 0; i < n; i++) {
            for (int j = i+1; j < n; j++) {
                q.push_back(make_pair(static_cast<float>(arr[i])/static_cast<float>(arr[j]), make_pair(arr[i], arr[j])));
                push_heap(q.begin(), q.end());

                if (q.size() > k) {
                    pop_heap(q.begin(), q.end());
                    q.pop_back();
                }
            }
        }
        return vector<int>{q.front().second.first, q.front().second.second};
    }
};
