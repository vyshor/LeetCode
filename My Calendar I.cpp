class MyCalendar {
public:
    vector<pair<int, int>> arr;
    MyCalendar() {

    }

    bool book(int start, int end) {
        auto p = make_pair(start, end);
        auto ptr = lower_bound(arr.begin(), arr.end(), p);
        int i = ptr - arr.begin();
        if (i != 0) {
            auto ptr2 = ptr - 1;
            if (ptr2->second > start) return false;
        }

        if (i != arr.size()) {
            if (ptr->first < end) return false;
        }

        arr.insert(ptr,p);
        return true;
    }
};

/**
 * Your MyCalendar object will be instantiated and called as such:
 * MyCalendar* obj = new MyCalendar();
 * bool param_1 = obj->book(start,end);
 */
