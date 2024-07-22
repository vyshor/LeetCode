class Solution {
public:
    struct Person
    {
        int h;
        string n;

        Person(int k, const std::string& s) : h(k), n(s) {}

        bool operator < (const Person& other) const
        {
            return (h > other.h);
        }
    };

    vector<string> sortPeople(vector<string>& names, vector<int>& heights) {
        int n = names.size();
        vector<Person> p;
        p.reserve(n);
        for (int i = 0; i < n; i++) {
            p.emplace_back(heights[i], names[i]);
        }

        sort(p.begin(), p.end());
        vector<string> arr;
        for (int i = 0; i < n; i++) {
            arr.push_back(move(p[i].n));
        }
        return arr;
    }
};
