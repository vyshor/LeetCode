func findJudge(n int, trust [][]int) int {
    people := make(map[int]interface{})
    for i := 1; i<n+1; i++ {
        people[i] = nil
    }
    trusted := make(map[int]map[int]interface{})
    for _, pair := range trust {
        person := pair[0]
        target := pair[1]
        if _, ok := people[person]; ok {
            delete(people, person)
        }

        if _, ok := trusted[target]; !ok {
            trusted[target] = map[int]interface{}{person: nil}
        } else {
            trusted[target][person] = nil
        }
    }

    if len(people) > 1 || len(people) == 0 {
        return -1
    }

    var judge int
    for k, _ := range people {
        judge = k
    }

    if judge == 1 && n == 1{
        return judge
    }

    if _, ok := trusted[judge]; ok && len(trusted[judge]) == n-1 {
        return judge
    }

    return -1
}
