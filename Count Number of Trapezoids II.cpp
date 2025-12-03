struct Line {
    int idx0;
    int idx1;
    int64_t midhash;
    int gradsign = 0;
    int gradtop;
    int gradbot;
    int64_t csign = 0;
    int64_t ctop = 0;
    int64_t cbot = 0;

    Line(vector<int>& pointA, vector<int>& pointB, int iA, int iB) :  idx0{iA}, idx1{iB}, midhash{static_cast<int64_t>(pointA[0]+pointB[0])*int64_t(1'000'000) + static_cast<int64_t>(pointA[1] + pointB[1])}, gradtop{pointA[1]-pointB[1]}, gradbot{pointA[0]-pointB[0]} {
        if (gradbot == 0) {
            gradtop = 1;
            ctop = 1;
            cbot = 0;
        }

        if (gradtop == 0) {
            gradbot = 1;
        }

        gradsign |= (gradtop < 0) ^ (gradbot < 0);
        gradtop = std::abs(gradtop);
        gradbot = std::abs(gradbot);

        int minn = min(gradtop, gradbot);
        for (int i{2}; i <= minn; ++i) {
            while ((gradtop % i == 0) && (gradbot % i == 0)) {
                gradtop /= i;
                gradbot /= i;
            }
            minn = min(minn, gradtop);
            minn = min(minn, gradbot);
        }

        // y = mx + c
        // c = y-mx
        ctop = pointA[1]*gradbot - ((gradsign) ? -gradtop*pointA[0]: gradtop*pointA[0]);
        csign = gradsign ^ (ctop < 0);
        cbot = gradbot;
        ctop = std::abs(ctop);

        int64_t minn2 = min(ctop, cbot);
        for (int64_t i{2}; i <= minn2; ++i) {
            while ((ctop % i == 0) && (cbot % i == 0)) {
                ctop /= i;
                cbot /= i;
            }
            minn2 = min(minn2, ctop);
            minn2 = min(minn2, cbot);
        }

        // cout << "idx0=" << idx0 << ",idx1=" << idx1 << ", grad=" << gradtop << "/" << gradbot << ",sign=" << gradsign;
        // cout << ", c=" << ctop << "/" << cbot << ",sign=" << gradsign << '\n';
    }

    int gradhash() {
        // Max gradtop, gradbot = 2000
        return (gradsign << 22) | (gradtop << 11) | gradbot;
    }

    int64_t chash() {
        return (csign << 63) | (ctop << 32) | cbot;
    }
};

class Solution {
public:
    int countTrapezoids(vector<vector<int>>& points) {
        int n = points.size();
        unordered_map<int, vector<Line*>> gradmapping;
        unordered_map<int64_t, vector<Line*>> midmapping;
        for (int i{0}; i < n-1; ++i) {
            for (int j{i+1};j < n; ++j) {
                auto line = new Line{points[i], points[j], i, j};
                gradmapping[line->gradhash()].push_back(line);
                midmapping[line->midhash].push_back(line);
            }
        }

        int ans{0};
        for (auto& [_, lines]: gradmapping) {
            int n2 = lines.size();
            if (n2 == 1) continue;

            int count{0};
            unordered_map<int64_t, int> counter;
            for (int i{0}; i < n2; ++i) {
                Line* line = lines[i];
                ans += count-counter[line->chash()];
                ++count;
                ++counter[line->chash()];
            }
        }

        for (auto& [_, lines]: midmapping) {
            int n2 = lines.size();
            if (n2 == 1) continue;

            int count{0};
            unordered_map<int, int> counter;
            for (int i{0}; i < n2; ++i) {
                Line* line = lines[i];
                ans -= count-counter[line->gradhash()];
                ++count;
                ++counter[line->gradhash()];
            }
        }

        return ans;
    }
};