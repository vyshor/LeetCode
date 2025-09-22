func matchPlayersAndTrainers(players []int, trainers []int) int {
    sort.Ints(players)
    sort.Ints(trainers)

    n := len(players)
    m := len(trainers)
    pidx, tidx := 0, 0
    count := 0
    for pidx < n {
        for tidx < m && players[pidx] > trainers[tidx] {
            tidx++
        }

        if (tidx < m && players[pidx] <= trainers[tidx]) {
            tidx++
            count++
        }
        pidx++
    }
    return count
}
