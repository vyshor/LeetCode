func abs(i int) int {
    if i < 0 {
        return -i
    }
    return i
}

func minMovesToSeat(seats []int, students []int) int {
    sort.Ints(seats)
    sort.Ints(students)
    n := len(seats)
    summ := 0
    for i := 0; i < n; i++ {
        summ += abs(seats[i]-students[i])
    }
    return summ
}
