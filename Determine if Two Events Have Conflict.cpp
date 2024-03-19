class Solution {
public:
    int convertTime(string s) {
        int i = stoi(s.substr(0, 2));
        int j = stoi(s.substr(3, 2));
        return i*60+j;
    }

    bool haveConflict(vector<string>& event1, vector<string>& event2) {
        int first_start=convertTime(event1.at(0)), first_end=convertTime(event1.at(1));
        int second_start=convertTime(event2.at(0)), second_end=convertTime(event2.at(1));
        if (first_start < second_start) return (first_end >= second_start);
        return (second_end >= first_start);
    }
};
