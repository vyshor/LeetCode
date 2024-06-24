func minKBitFlips(nums []int, k int) int {
    n := len(nums)
    q := make([]int, k+1)
    var i, j, l, count, xorr int
    for i < n {
        // fmt.Println(j, l, q)
        if j != l && q[j] <= i {
            j++
            j %= (k+1)
            xorr ^= 1
        }

        if nums[i] ^ xorr == 0 {
            if i > n-k {
                return -1
            }

            xorr ^= 1
            count++
            q[l] = i+k
            l++
            l %= (k+1)
        }
        i++
    }
    return count
}

