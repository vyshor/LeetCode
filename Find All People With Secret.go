func findAllPeople(n int, meetings [][]int, firstPerson int) []int {
    known := map[int]interface{}{
        0: nil,
        firstPerson: nil,
    }

    sort.Slice(meetings, func(i, j int) bool {
        return meetings[i][2] < meetings[j][2]
    })

    var prev_t int
    dp := make(map[int][]int)
    for _, meeting := range meetings {
        x := meeting[0]
        y := meeting[1]
        t := meeting[2]

        if t != prev_t {
            dp = make(map[int][]int)
            prev_t = t
        }

        _, ok_x := known[x]
        _, ok_y := known[y]
        if !ok_x && !ok_y {
            if _, ok := dp[x]; !ok {
                dp[x] = []int{y}
            } else {
                dp[x] = append(dp[x], y)
            }

            if _, ok := dp[y]; !ok {
                dp[y] = []int{x}
            } else {
                dp[y] = append(dp[y], x)
            }

        } else {
            q := []int{x, y}
            i := 0
            for i < len(q) {
                person := q[i]

                known[person] = nil
                if _, ok := dp[person]; ok {
                    for _, other_person := range dp[person] {
                        if _, ok := dp[other_person]; ok {
                            q = append(q, other_person)
                        }
                    }
                    delete(dp, person)
                }
                i++
            }
        }
    }
    ans := make([]int, len(known))
    i := 0
    for val := range known {
        ans[i] = val
        i++
    }
    return ans
}
