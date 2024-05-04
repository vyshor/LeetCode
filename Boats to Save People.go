func numRescueBoats(people []int, limit int) int {
    sort.Ints(people)
    var count, i int
    j := len(people) - 1
    for i <= j {
        other := limit - people[i]
        for i < j && people[j] > other {
            j--
            count++
        }

        if i < j && people[j]<= limit {
            j--
        }

        count++
        i++
    }
    return count
}
