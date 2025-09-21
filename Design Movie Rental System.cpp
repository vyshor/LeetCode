struct mov {
    int price;
    int shop;
    int id;
    bool rented;
};

struct mov2 {
    mov* ptr;

    bool operator>(const mov2& other) const {
        if (ptr->price == other.ptr->price) {
            if (ptr->shop == other.ptr->shop) {
                return ptr->id > other.ptr->id;
            } else {
                return ptr->shop > other.ptr->shop;
            }
        } else{
            return ptr->price > other.ptr->price;
        }
    };
};

class MovieRentingSystem {
public:
    unordered_map<int64_t, mov> all_movies;
    vector<mov2> cheap_rented;
    unordered_map<int, vector<mov2>> cheap_unrented;

    MovieRentingSystem(int n, vector<vector<int>>& entries) {
        for (auto& entry: entries) {
            int shop = entry[0];
            int movie = entry[1];
            int price = entry[2];

            int64_t k = key(movie, shop);
            all_movies[k] = mov(price, shop, movie, false);
            cheap_unrented[movie].emplace_back(&all_movies[k]);
            push_heap(cheap_unrented[movie].begin(), cheap_unrented[movie].end(),  std::greater<>{});
        }
    }

    int64_t key(int movie, int shop) {
        return (int64_t(movie) << 32) | int64_t(shop);
    }

    vector<int> search(int movie) {
        vector<mov2>& h = cheap_unrented[movie];
        vector<int> results;
        vector<mov2> tmp;
        unordered_set<int64_t> keys;

        int topN = 5;
        while (h.size() > 0 && topN > 0) {
            pop_heap(h.begin(), h.end(), std::greater<>{});
            mov2 movie = std::move(h.back());
            h.pop_back();

            if (movie.ptr->rented) continue;
            int64_t k = key(movie.ptr->id, movie.ptr->shop);
            if (keys.contains(k)) continue;
            keys.insert(k);

            results.push_back(movie.ptr->shop);
            tmp.push_back(std::move(movie));
            topN--;
        }

        for (auto& movie: tmp) {
            h.push_back(std::move(movie));
            push_heap(h.begin(), h.end(),  std::greater<>{});
        }
        return results;
    }

    void rent(int shop, int movie) {
        int64_t k = key(movie, shop);
        all_movies[k].rented = true;
        cheap_rented.emplace_back(&all_movies[k]);
        push_heap(cheap_rented.begin(), cheap_rented.end(), std::greater<>{});
    }

    void drop(int shop, int movie) {
        int64_t k = key(movie, shop);
        all_movies[k].rented = false;
        cheap_unrented[movie].emplace_back(&all_movies[k]);
        push_heap(cheap_unrented[movie].begin(), cheap_unrented[movie].end(), std::greater<>{});
    }

    vector<vector<int>> report() {
        vector<mov2>& h = cheap_rented;
        vector<vector<int>> results;
        vector<mov2> tmp;
        unordered_set<int64_t> keys;

        int topN = 5;
        while (h.size() > 0 && topN > 0) {
            pop_heap(h.begin(), h.end(), std::greater<>{});
            mov2 movie = std::move(h.back());
            h.pop_back();

            if (!movie.ptr->rented) continue;
            int64_t k = key(movie.ptr->id, movie.ptr->shop);
            if (keys.contains(k)) continue;
            keys.insert(k);

            results.push_back({movie.ptr->shop, movie.ptr->id});
            tmp.push_back(std::move(movie));
            topN--;
        };

        for (auto& movie: tmp) {
            h.push_back(std::move(movie));
            push_heap(h.begin(), h.end(),  std::greater<>{});
        }
        return results;
    }
};

/**
 * Your MovieRentingSystem object will be instantiated and called as such:
 * MovieRentingSystem* obj = new MovieRentingSystem(n, entries);
 * vector<int> param_1 = obj->search(movie);
 * obj->rent(shop,movie);
 * obj->drop(shop,movie);
 * vector<vector<int>> param_4 = obj->report();
 */