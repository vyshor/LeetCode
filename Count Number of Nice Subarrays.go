func numberOfSubarrays(nums []int, k int) int {
    n := len(nums)
    count := 0
    prefix := make([]int, 0)
    subfix := make([]int, 0)
    for _, num := range nums {
        if num % 2 == 1 {
            prefix = append(prefix, count)
            count = 1
        } else {
            count += 1
        }
    }

    if count > 0 {
        prefix = append(prefix, count)
    }

    count = 0
    for i := n-1; i > -1; i-- {
        if nums[i] % 2 == 1 {
            subfix = append(subfix, count)
            count = 1
        } else {
            count += 1
        }
    }

    if count > 0 {
        subfix = append(subfix, count)
    }

    i, j := k, len(subfix) - 1
    summ := 0
    for i < len(prefix) {
        summ += prefix[i] * subfix[j]
        i++
        j--
    }
    return summ
}

