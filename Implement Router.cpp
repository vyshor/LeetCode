struct packet {
    int source;
    int destination;
    int timestamp;

    bool operator<(const packet& other) const {
        return timestamp < other.timestamp;
    }

    string toString() {
        return to_string(source) + " " + to_string(destination) + " " + to_string(timestamp);
    }
};

class Router {
public:
    int limit;
    deque<packet> dq;
    unordered_map<int, deque<packet>> counter;
    unordered_set<string> seen;

    Router(int memoryLimit) {
        limit = memoryLimit;
    }

    bool addPacket(int source, int destination, int timestamp) {
        packet p(source, destination, timestamp);
        string hash = p.toString();

        if (seen.contains(hash)) return false;
        seen.insert(hash);

        if (dq.size() == limit) {
            auto p2 = dq.front();
            seen.erase(p2.toString());
            dq.pop_front();
            counter[p2.destination].pop_front();
        }

        dq.push_back(p);
        counter[destination].push_back(p);
        return true;
    }

    vector<int> forwardPacket() {
        if (dq.size() == 0) return {};

        auto p = dq.front();
        seen.erase(p.toString());
        dq.pop_front();
        counter[p.destination].pop_front();
        return {p.source, p.destination, p.timestamp};
    }

    int getCount(int destination, int startTime, int endTime) {
        if (!counter.contains(destination)) return 0;

        auto& q = counter[destination];
        auto start_packet = packet(0, 0, startTime);
        auto end_packet = packet(0, 0, endTime);
        auto sidx = lower_bound(q.begin(), q.end(), start_packet) - q.begin();
        auto eidx = upper_bound(q.begin(), q.end(), end_packet) - q.begin();
        // cout << sidx << " " << eidx;
        return eidx - sidx;
    }
};

/**
 * Your Router object will be instantiated and called as such:
 * Router* obj = new Router(memoryLimit);
 * bool param_1 = obj->addPacket(source,destination,timestamp);
 * vector<int> param_2 = obj->forwardPacket();
 * int param_3 = obj->getCount(destination,startTime,endTime);
 */