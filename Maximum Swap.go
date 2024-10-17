func maximumSwap(num int) int {
    nums := strconv.Itoa(num)
    n := len(nums)
    i := 1
    spot := 0
    found := false
    maxx := byte('0')
    j := 0
    for i < n {
        if !found {
            if nums[i] > nums[i-1] {
                found = true
                maxx = nums[i]
                j = i
            } else if nums[i] < nums[i-1] {
                spot = i
            }
        } else {
            if nums[i] >= maxx {
                maxx = nums[i]
                j = i
            }
        }
        i++
    }

    if found {
        i = 0
        for i < spot {
            if nums[i] < maxx {
                 spot = i
            }
            i++
        }
        arr := []byte(nums)
        arr[spot], arr[j] = arr[j], arr[spot]
        num, _ = strconv.Atoi(string(arr))
    }
    return num
}
