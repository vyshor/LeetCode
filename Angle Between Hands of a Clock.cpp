class Solution {
public:
    double angleClock(int hour, int minutes) {
        hour %= 12;
        double h = static_cast<double>(hour);
        double m = static_cast<double>(minutes);
        // m/60 * 360
        double min_angle = m * 6.;
        // h*30 + m/60 * 30
        double hour_angle = h * 30. + 0.5*m;
        double diff = abs(hour_angle-min_angle);
        // cout << "h=" << hour_angle << " m=" << min_angle << endl;
        return min(diff, 360.-diff);
    }
};
