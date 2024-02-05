class Solution {
public:
    int firstUniqChar(string s) {
        unordered_map<char, int> umap;
        for(char& c : s) {
            if (umap.find(c) == umap.end()) {
                umap.insert(make_pair(c, 1));
            } else {
                umap.at(c)++;
            }
        }

        int i = 0;
        for(char& c : s) {
            if (umap.at(c) == 1) return i;
            i++;
        }
        return -1;
    }
};
