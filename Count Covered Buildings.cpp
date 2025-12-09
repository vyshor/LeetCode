class Solution {
public:
    int countCoveredBuildings(int n, vector<vector<int>>& buildings) {
        int m = buildings.size();
        std::sort(buildings.begin(), buildings.end());
        vector<int> covered_buildings(m, 1);
        vector<int> cover_x(n+1, 0);
        vector<int> cover_y(n+1, 0);
        for (int i{0}; i < m; ++i) {
            int x = buildings[i][0];
            int y = buildings[i][1];
            if (!cover_x[x]) {
                cover_x[x] = 1;
                covered_buildings[i] = 0;
            }

            if (!cover_y[y]) {
                cover_y[y] = 1;
                covered_buildings[i] = 0;
            }
        }

        // std::cout << "Covered building=";
        // for (int i{0}; i < m; ++i) {
        //     std::cout << ' ' << covered_buildings[i];
        // }
        // std::cout << '\n';

        vector<int> cx(n+1, 0);
        vector<int> cy(n+1, 0);
        cover_x.swap(cx);
        cover_y.swap(cy);

        for (int i{m-1}; i >= 0; --i) {
            int x = buildings[i][0];
            int y = buildings[i][1];
            if (!cover_x[x]) {
                cover_x[x] = 1;
                covered_buildings[i] = 0;
            }

            if (!cover_y[y]) {
                cover_y[y] = 1;
                covered_buildings[i] = 0;
            }
        }
        int total = 0;
        for (int i{0}; i < m; ++i) {
            total += covered_buildings[i];
        }
        return total;
    }
};
