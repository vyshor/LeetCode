struct cls {
    double inc;
    int t;
    int p;

    bool operator<(const cls& other) const {
        return inc < other.inc;
    }
};

class Solution {
public:
    double maxAverageRatio(vector<vector<int>>& classes, int extraStudents) {
        double tc = classes.size(), i = extraStudents;
        double summ = 0;
        vector<cls> h;
        h.reserve(tc);

        for (auto cur_class: classes) {
            auto pp = cur_class[0];
            auto tt = cur_class[1];

            if (pp == tt ) {
                summ += 1;
                continue;
            }
            double p = double(pp);
            double t = double(tt);
            h.emplace_back((p+1)/(t+1) - p/t, tt, pp);
        }
        if (h.size() == 0) return 1;

        std::make_heap(h.begin(), h.end());
        while (i > 0) {
            std::pop_heap(h.begin(), h.end());
            auto& cur = h.back();
            // cout << cur.t << " " << cur.p << endl;
            cur.t++;
            cur.p++;
            double p = double(cur.p);
            double t = double(cur.t);
            cur.inc = (p+1)/(t+1) - p/t;
            std::push_heap(h.begin(), h.end());
            i--;
        }

        for (auto& cur: h) {
            double p = double(cur.p);
            double t = double(cur.t);
            summ += p/t;
        }
        return summ / tc;
    }
};
