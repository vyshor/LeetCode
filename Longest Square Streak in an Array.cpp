class Solution {
public:
    int longestSquareStreak(vector<int>& nums) {
        unordered_set<int> nums1(nums.begin(), nums.end());
        vector<int> nums2(nums1.begin(), nums1.end());
        int n = nums2.size();
        int maxx = 1;
        unordered_map<int, int> terms;
        vector<int> parents(n);
        vector<int> counts(n, 1);
        for (int i = 0; i < n; i++) {
            terms[nums2[i]] = i;
            parents[i] = i;
        }
        function<int(int)> find;
        function<void(int, int)> uni;
        find = [&find, &parents] (int i) -> int {
            if (parents[i] != i) return find(parents[i]);
            return i;
        };

        uni = [&find, &parents, &counts, &maxx] (int i, int j) {
            int parent_i = find(i), parent_j = find(j);
            if (parent_i != parent_j) {
                parents[parent_i] = parent_j;
                counts[parent_j] += counts[parent_i];
                maxx = max(maxx, counts[parent_j]);
                counts[parent_i] = 0;
            }
        };

        for (int i = 0; i < n; i++) {
            // Check for overflow
            // Because 317 * 317 > 10^5
            if (nums2[i] >= 317) continue;

            int nxt = nums2[i] * nums2[i];
            if (terms.contains(nxt)) {
                uni(i, terms[nxt]);
            }
        }

        return (maxx == 1) ? -1 : maxx;
    }
};
