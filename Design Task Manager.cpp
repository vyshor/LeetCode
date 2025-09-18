struct taskh {
    int priority;
    int taskId;
    int userId;
    bool removed;
};

struct task {
    taskh* ptr;

    bool operator<(const task& other) const {
        return (ptr->priority == other.ptr->priority && ptr->taskId < other.ptr->taskId) || (ptr->priority < other.ptr->priority);
    };
};

class TaskManager {
public:
    vector<task> h;
    unordered_map<int, taskh*> m;

    TaskManager(vector<vector<int>>& tasks) {
        for (auto& t_list: tasks) {
            int userId = t_list[0];
            int taskId = t_list[1];
            int priority = t_list[2];

            taskh* newTaskh = new taskh(priority, taskId, userId, false);
            m[taskId] = newTaskh;
            h.emplace_back(newTaskh);
        }
        make_heap(h.begin(), h.end());
    }

    void add(int userId, int taskId, int priority) {
        taskh* newTaskh = new taskh(priority, taskId, userId, false);
        m[taskId] = newTaskh;
        h.emplace_back(newTaskh);
        push_heap(h.begin(), h.end());
    }

    void edit(int taskId, int newPriority) {
        m[taskId]->removed = true;
        int userId = m[taskId]->userId;
        taskh* newTaskh = new taskh(newPriority, taskId, userId, false);
        m[taskId] = newTaskh;
        h.emplace_back(newTaskh);
        push_heap(h.begin(), h.end());
    }

    void rmv(int taskId) {
        m[taskId]->removed = true;
        m.erase(taskId);
    }

    int execTop() {
        while (h.size() > 0) {
            pop_heap(h.begin(), h.end());
            auto t = h.back();
            h.pop_back();
            if (t.ptr->removed) {
                delete(t.ptr);
            } else {
                int userId = t.ptr->userId;
                int taskId = t.ptr->taskId;
                delete(t.ptr);
                return userId;
            }
        }
        return -1;
    }


};

/**
 * Your TaskManager object will be instantiated and called as such:
 * TaskManager* obj = new TaskManager(tasks);
 * obj->add(userId,taskId,priority);
 * obj->edit(taskId,newPriority);
 * obj->rmv(taskId);
 * int param_4 = obj->execTop();
 */
