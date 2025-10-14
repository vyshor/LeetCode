struct Trie {
    Trie* children[26];

    void add(string& word, int i) {
        if (i == word.size()) return;
        int idx = word[i]-97;
        if (!children[idx]) children[idx] = new Trie();
        children[idx]->add(word, i+1);
    }
};

class Solution {
public:
    int minValidStrings(vector<string>& words, string target) {
        Trie root;
        for (string& word: words) {
            root.add(word, 0);
        }

        int n = target.size();
        vector<int> dp(n+1, INT_MAX);
        dp[n] = 0;

        for (int i = n-1; i >= 0; i--) {
            int j = i;
            int ch = target[j]-97;
            Trie* ptr = root.children[ch];
            while (j < n && ptr) {
                // cout << "i=" << i << " j=" << j << endl;
                if (dp[j+1] != INT_MAX) dp[i] = min(dp[i], 1+dp[j+1]);

                j++;
                if (j < n) {
                    ch = target[j]-97;
                    ptr = ptr->children[ch];
                }
            }
        }
        if (dp[0] == INT_MAX) return -1;
        return dp[0];
    }
};
