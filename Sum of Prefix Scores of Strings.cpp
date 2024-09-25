class Node {
public:
    unordered_map<char, Node> route;
    int score = 0;
    Node() {};
    void add(string& word, int idx) {
        if (word.size() == idx) {
            return;
        }

        auto c = word[idx];
        if (!route.contains(c)) route[c] = Node();
        route[c].score++;
        route[c].add(word, idx+1);
    }

    int find(string& word, int idx) {
        if (word.size() == idx) return score;

        auto c = word[idx];
        if (!route.contains(c)) return score;
        return score + route[c].find(word, idx+1);
    }
};

class Solution {
public:
    vector<int> sumPrefixScores(vector<string>& words) {
        auto trie = Node();
        for (auto word: words) {
            trie.add(word, 0);
        }

        vector<int> arr;
        arr.reserve(words.size());
        for (auto word: words) {
            arr.push_back(trie.find(word, 0));
        }
        return arr;
    }
};
