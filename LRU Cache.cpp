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

class LRUCache {
public:
    int cap{0};
    int counter{0};
    std::unordered_map<int, pair<int, int>> mapping; // Key -> fval, val
    std::set<pair<int, int>> usages; // fval, key

    LRUCache(int capacity) : cap(capacity) {
    }

    int get(int key) {
        if (mapping.contains(key)) {
            int value = mapping[key].second;
            usages.erase(make_pair(mapping[key].first, key));
            int fval = ++counter;
            mapping[key] = std::make_pair(fval, value);
            usages.emplace(fval, key);
            return mapping[key].second;
        }
        return -1;
    }

    void put(int key, int value) {
        if (!mapping.contains(key)) {
            if (mapping.size() == cap) {
                auto smallest_pair = *usages.begin();
                usages.erase(smallest_pair);
                mapping.erase(smallest_pair.second);
            }
        } else {
            usages.erase(make_pair(mapping[key].first, key));
        }

        int fval = ++counter;
        mapping[key] = std::make_pair(fval, value);
        usages.emplace(fval, key);
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */
