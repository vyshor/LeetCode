class Solution {
public:
    int numRescueBoats(vector<int>& people, int limit) {
        sort(people.begin(), people.end());
        int count = 0, i = 0, j = people.size() - 1;
        while (i <= j) {
            int other = limit - people[i];
            while (i < j && people[j] > other) {
                j--;
                count++;
            }

            if (i < j && people[j] <= limit) j--;

            count++;
            i++;
        }

        return count;
    }
};
