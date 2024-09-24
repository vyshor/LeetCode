class Node {
public:
    unordered_map<char, Node> route;
    bool end = false;
    Node() {};
    void add(string& word, int idx) {
        if (word.size() == idx) {
            end = true;
            return;
        }

        auto c = word[idx];
        if (!route.contains(c)) route[c] = Node();
        route[c].add(word, idx+1);
    }

    int find(string& word, int idx) {
        if (word.size() == idx) return word.size();

        auto c = word[idx];
        if (!route.contains(c)) return idx;
        return route[c].find(word, idx+1);
    }
};

class Solution {
public:
    int longestCommonPrefix(vector<int>& arr1, vector<int>& arr2) {
        auto trie = Node();
        for (int i: arr1) {
            auto word = to_string(i);
            trie.add(word, 0);
        }

        int maxx = 0;
        for (int i: arr2) {
            auto word = to_string(i);
            maxx = max(maxx, trie.find(word, 0));
        }

        return maxx;
    }
};
