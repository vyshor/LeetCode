struct Trie {
    Trie* children[26];

    int hotpath;
    vector<string_view> suggestions;

    void add(int i, string_view word, bool is_hot = false) {
        if (i == word.size()) return;

        int ch = word[i] - 97;
        if (!children[ch]) {
            children[ch] = new Trie();
        }
        children[ch]->hotpath = is_hot;

        if (!is_hot) {
            vector<string_view>& sugg = children[ch]->suggestions;
            sugg.push_back(word);
            push_heap(sugg.begin(), sugg.end());
            if (sugg.size() > 3) {
                pop_heap(sugg.begin(), sugg.end());
                sugg.pop_back();
            }
        }

        children[ch]->add(i+1, word, is_hot);
    }
};

class Solution {
public:
    vector<vector<string>> suggestedProducts(vector<string>& products, string searchWord) {
        Trie root;
        root.add(0, searchWord, true);
        for (string_view product: products) {
            root.add(0, product, false);
        }

        vector<vector<string>> ans;
        Trie* ptr = &root;
        int n = searchWord.size();
        for (int i = 0; i < n; i++) {
            int ch = searchWord[i] - 97;
            ptr = ptr->children[ch];
            auto& sugg = ptr->suggestions;
            sort(sugg.begin(), sugg.end());
            ans.emplace_back(sugg.begin(), sugg.end());
        }
        return ans;
    }
};
