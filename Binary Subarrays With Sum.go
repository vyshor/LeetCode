func numSubarraysWithSum(nums []int, goal int) int {
    if goal == 0 {
        combo := 0
        total := 0
        for _, num := range nums {
            if num == 1 && combo > 0 {
                total += (combo * (combo+1))/2
                combo = 0
            } else if num == 0 {
                combo++
            }
        }

        if combo > 0 {
            total +=  (combo * (combo+1))/2
        }

        return total
    }

    arr := make([]int, 0)
    combo := 1
    for _, num := range nums {
        if num == 1 {
            arr = append(arr, combo)
            combo = 1
        } else {
            combo++
        }
    }
    arr = append(arr, combo)
    left := 0
    right := goal
    total := 0
    for right < len(arr) {
        total += arr[right] * arr[left]
        right++
        left++
    }
    return total
}
