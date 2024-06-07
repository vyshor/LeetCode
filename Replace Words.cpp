class Trie {
public:
    Trie() {}

    bool is_word = false;
    map<char, Trie> paths;

    void add(int i, string& word) {
        if (i == word.size()) {
            is_word = true;
            return;
        }

        char& c = word[i];
        if (!paths.contains(c)) paths[c] = Trie();
        paths[c].add(i+1, word);
    }

    string search(int i, string& word) {
        if (is_word) return word.substr(0, i);
        if (i == word.size() || !paths.contains(word[i])) return word;
        return paths[word[i]].search(i+1, word);
    }
};

class Solution {
public:
    vector<string> getWords(string s){
        vector<string> res;
        int pos = 0;
        while(s.size() > 0){
            pos = s.find(' ');
            if (pos != s.npos) {
                res.push_back(s.substr(0,pos));
                s.erase(0,pos+1);
            } else {
                res.push_back(s);
                s = "";
            }
        }
        return res;
    }


    string replaceWords(vector<string>& dictionary, string sentence) {
        Trie root = Trie();
        for (string& word: dictionary) {
            root.add(0, word);
        }

        stringstream ss;
        vector<string> words = getWords(sentence);
        for (string& word : words) {
            ss << root.search(0, word);
            ss << ' ';
        }

        string ans_str = ss.str();
        ans_str.erase(ans_str.size()-1);
        return ans_str;
    }
};
