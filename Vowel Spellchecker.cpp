class Solution {
public:
    vector<string> spellchecker(vector<string>& wordlist, vector<string>& queries) {
        size_t n = wordlist.size();
        vector<string> results;
        results.reserve(queries.size());

        unordered_set<string> exacts;
        unordered_map<string, string> lower;
        unordered_map<string, string> vowels;
        unordered_set<char> vow{'a', 'e', 'i', 'o', 'u'};

        for (int i = n-1; i >= 0; i--) {
            string exact = wordlist[i];
            string word = exact;
            string v = word;

            char* ptr = word.data();
            char* vptr = v.data();

            size_t m = exact.size();
            for (size_t j = 0; j < m; j++) {
                if (int(*(ptr+j)) < 97) {
                    *(ptr+j) += 32;
                    *(vptr+j) += 32;
                }

                if (vow.contains(*(ptr+j))) {
                    *(vptr+j) = 64;
                }
            }

            exacts.insert(exact);
            lower[word] = exact;
            vowels[v] = exact;

            // cout << "Exact: " << exact << " Lower: " << word << " Vowels: " << v << endl;
        }

        for (auto& query: queries) {
            if (exacts.contains(query)) {
                results.push_back(query);
                continue;
            }

            string word = query;
            string v = word;

            char* ptr = word.data();
            char* vptr = v.data();

            size_t m = query.size();
            for (size_t j = 0; j < m; j++) {
                if (int(*(ptr+j)) < 97) {
                    *(ptr+j) += 32;
                    *(vptr+j) += 32;
                }

                if (vow.contains(*(ptr+j))) {
                    *(vptr+j) = 64;
                }
            }

            if (lower.contains(word)) {
                results.push_back(lower[word]);
            } else if (vowels.contains(v)) {
                results.push_back(vowels[v]);
            } else {
                results.push_back("");
            }
        }
        return results;
    }
};
