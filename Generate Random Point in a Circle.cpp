class Solution {
public:
    double x;
    double y;
    double r;
    uniform_real_distribution<double> unif;
    uniform_real_distribution<double> unif2;
    default_random_engine re;

    Solution(double radius, double x_center, double y_center) {
        r = radius;
        x = x_center;
        y = y_center;
        unif = uniform_real_distribution<double>(0.f, 2*M_PI);
        unif2 = uniform_real_distribution<double>(0.f, 1.0f);
    }

    vector<double> randPoint() {
        double random_angle = unif(re);
        double R = r*sqrt(unif2(re));
        // if (cos(random_angle) >= 1.0f || sin(random_angle) >= 1.0f) {
        //     cout << random_angle << " " << cos(random_angle) << " " << sin(random_angle) << endl;
        // }

        return {x+R*cos(random_angle), y+R*sin(random_angle)};
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(radius, x_center, y_center);
 * vector<double> param_1 = obj->randPoint();
 */
