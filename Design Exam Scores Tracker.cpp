class ExamTracker {
public:
    long long total_score = 0;
    vector<long long> scores;
    vector<int> timeslots;

    ExamTracker() {

    }

    void record(int time, int score) {
        timeslots.push_back(time-1);
        scores.push_back(total_score);
        total_score += score;
        scores.push_back(total_score);
        timeslots.push_back(time);
    }

    long long totalScore(int startTime, int endTime) {
        int start = lower_bound(timeslots.begin(), timeslots.end(), startTime-1) - timeslots.begin();
        int end = lower_bound(timeslots.begin(), timeslots.end(), endTime) - timeslots.begin();
        return scores[end] - scores[start];
    }
};

/**
 * Your ExamTracker object will be instantiated and called as such:
 * ExamTracker* obj = new ExamTracker();
 * obj->record(time,score);
 * long long param_2 = obj->totalScore(startTime,endTime);
 */
