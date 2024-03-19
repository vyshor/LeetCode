func convertTime(s string) int {
    arr := strings.Split(s, ":")
    i, _ := strconv.Atoi(arr[0])
    j, _ := strconv.Atoi(arr[1])
    return i*60+j
}

func haveConflict(event1 []string, event2 []string) bool {
    first_start := convertTime(event1[0])
    first_end := convertTime(event1[1])

    second_start := convertTime(event2[0])
    second_end := convertTime(event2[1])
    if first_start < second_start {
        return first_end >= second_start
    }
    return second_end >= first_start
}
