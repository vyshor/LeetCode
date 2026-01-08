class LRUCache {
public:
    int cap{0};
    int counter{0};
    std::unordered_map<int, int> mapping;
    std::unordered_map<int, int> freshness;
    std::vector<pair<int, int>> usages;

    LRUCache(int capacity) : cap(capacity) {
    }

    int get(int key) {
        if (mapping.contains(key)) {
            int fval = ++counter;
            usages.emplace_back(fval, key);
            push_heap(usages.begin(), usages.end(), std::greater<>{});
            freshness[key] = fval;
            return mapping[key];
        }
        return -1;
    }

    void put(int key, int value) {
        if (!mapping.contains(key)) {
            while (mapping.size() == cap) {
                pop_heap(usages.begin(), usages.end(), std::greater<>{});
                auto [fval, old_key] = std::move(usages.back());
                usages.pop_back();
                if (freshness[old_key] == fval) {
                    mapping.erase(old_key);
                }
            }
        }

        mapping[key] = value;
        int fval = ++counter;
        usages.emplace_back(fval, key);
        push_heap(usages.begin(), usages.end(), std::greater<>{});
        freshness[key] = fval;

    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */

