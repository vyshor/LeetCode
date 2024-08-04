func rangeSum(nums []int, n int, left int, right int) int {
    MOD := 1000000007
    prefix := make([]int, n+1)
    suffix := make([]int, n+1)
    summ := 0
    for i := 0; i < n; i++ {
        summ += nums[i]
        prefix[i+1] = summ
    }

    total := summ
    summ = 0
    for i := n-1; i >= 0; i-- {
        summ += nums[i]
        suffix[i] = summ
    }

    arr := make([]int, 0)
    for i := 0; i < n; i++ {
        for j := i; j < n; j++ {
            arr = append(arr, (total - prefix[i] - suffix[j+1]))
        }
    }
    sort.Ints(arr)
    summ = 0
    for i := left-1; i < right; i++ {
        summ += arr[i]
        summ %= MOD
    }
    return summ
}
