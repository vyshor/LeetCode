class UndergroundSystem {
public:
    unordered_map<int, pair<string, int>> customer_statuses;
    unordered_map<string, double> summ;
    unordered_map<string, int64_t> count;

    UndergroundSystem() {}

    void checkIn(int id, string stationName, int t) {
        customer_statuses[id] = {stationName, t};
    }

    void checkOut(int id, string stationName, int t) {
        auto& [inStation, t_in] = customer_statuses[id];
        string key = inStation + "-" + stationName;
        double diff = double(t) - double(t_in);
        summ[key] += diff;
        count[key]++;
    }

    double getAverageTime(string startStation, string endStation) {
        string key = startStation + "-" + endStation;
        return summ[key] / double(count[key]);
    }
};

/**
 * Your UndergroundSystem object will be instantiated and called as such:
 * UndergroundSystem* obj = new UndergroundSystem();
 * obj->checkIn(id,stationName,t);
 * obj->checkOut(id,stationName,t);
 * double param_3 = obj->getAverageTime(startStation,endStation);
 */