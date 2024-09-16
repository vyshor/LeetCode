func convert(s string) int {
    a, _ := strconv.Atoi(s[:2])
    b, _ := strconv.Atoi(s[3:])
    return a * 60 + b
}

func findMinDifference(timePoints []string) int {
    arr := make([]int, 0)
    for _, tp := range timePoints {
        arr = append(arr, convert(tp))
    }
    sort.Ints(arr)
    minn := arr[0] + 24 * 60 - arr[len(arr)-1]
    for i := 0; i < len(arr)-1; i++ {
        minn = min(minn, arr[i+1]-arr[i])
    }
    return minn
}
