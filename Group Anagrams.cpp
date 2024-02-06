class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> umap;
        vector<vector<string>> ans;
        for (string & s: strs) {
            char arr[27];
            fill_n(arr, 27, ' ');

            arr[26] = '\0';
            for (char & c: s) {
                arr[c-97]++;
            }
            if (umap.find(arr) == umap.end()) {
                vector<string> vect{ s };
                umap.insert(make_pair(arr, vect));
            } else {
                umap.at(arr).push_back(s);
            }
        }

        for (auto& it: umap) {
            ans.push_back(it.second);
        }
        return ans;
    }
};
