class Solution {
public:
    vector<string> findRelativeRanks(vector<int>& score) {
        vector<int> arr = score;
        sort(arr.begin(), arr.end());
        int n = arr.size();
        unordered_map<int, string> scores;
        vector<string> names{"Gold Medal", "Silver Medal", "Bronze Medal"};

        for (int i = 0; i < n; i++) {
            int j = n-1-i;
            if (i < 3) {
                scores[arr[j]] = names[i];
            } else {
                scores[arr[j]] = to_string(i+1);
            }
        }

        vector<string> ans;
        ans.reserve(n);
        for (int i=0; i<n; i++) {
            ans.push_back(scores[score[i]]);
        }
        return ans;
    }
};
