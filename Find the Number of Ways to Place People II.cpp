class Solution {
public:
    int numberOfPairs(vector<vector<int>>& points) {
        sort(points.begin(), points.end(), [](const vector<int>& a, const vector<int>& b) {
            return  (a[1] > b[1]) || (a[1] == b[1] && a[0] < b[0]);
        });
        int n = points.size();
        int count = 0;
        vector<tuple<int,int,int>> x_points;
        for (int i = 0; i < n; i++) {
            auto& pt = points[i];
            // cout << pt[0] << " " << pt[1] << endl;
            x_points.push_back({pt[0], pt[1], i});
        }

        sort(x_points.begin(), x_points.end(),[](const tuple<int,int,int>& a, const tuple<int,int,int>& b) {
            return  (get<0>(a) < get<0>(b)) || ((get<0>(a) == get<0>(b)) && (get<1>(a) > get<1>(b)));
        });
        unordered_map<int, int> ptmap;
        for (int i = 0; i < n; i++) {
            auto& pt = x_points[i];
            ptmap[get<2>(pt)] = i;
        }

        for (int i = 0; i < n-1; i++) {
            for (int j = i+1; j < n; j++) {
                if (points[i][0] > points[j][0]) continue;

                bool valid_pair = true;
                for (int k = ptmap[i]+1; k < ptmap[j]; k++) {
                    int container_pt_y = points[get<2>(x_points[k])][1];
                    if (container_pt_y <= points[i][1] && container_pt_y >= points[j][1]) {
                        valid_pair = false;
                        break;
                    }
                }
                count += valid_pair;
            }
        }

        return count;
    }
};