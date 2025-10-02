class Trie {
    public:

    int val = 0;
    vector<Trie*> children;

    Trie(int v = 0) {
        val = v;
        children.resize(26);
    }

    int find(string& ss, int idx) {
        if (idx < ss.size()) {
            int pos = ss[idx] - 97;
            auto child = children[pos];
            if (child) return child->find(ss, idx+1);
            return 0;
        } else {
            int summ = val;
            for (auto& child: children) {
                if (child) summ += child->find(ss, idx);
            }

            return summ;
        }
        return -1;
    }

    void add(string& ss, int idx, int v) {
        if (idx == ss.size()) {
            val = v;
            return;
        }

        int pos = ss[idx] - 97;
        if (!children[pos]) {
            children[pos] = new Trie();
        };
        children[pos]->add(ss, idx+1, v);
    }
};

class MapSum {
public:
    Trie root;

    MapSum() {
    }

    void insert(string key, int val) {
        root.add(key, 0, val);
    }

    int sum(string prefix) {
        return root.find(prefix, 0);
    }
};

/**
 * Your MapSum object will be instantiated and called as such:
 * MapSum* obj = new MapSum();
 * obj->insert(key,val);
 * int param_2 = obj->sum(prefix);
 */
