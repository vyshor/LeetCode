func maximumLength(nums []int, k int) int {
    count := make([]int, k*k)
    for _, num := range nums {
        r := num % k
        count[r*k+r]++

        for i := 0; i < k; i++ {
            if r == i {
                continue
            }

            count[i*k+r] += (count[i*k+r] ^ 1) & 1
        }

        for i := 0; i < k; i++ {
            if r == i {
                continue
            }

            count[r*k+i] += count[r*k+i] & 1
        }
    }
    return max(slices.Max(count), 2)
}
