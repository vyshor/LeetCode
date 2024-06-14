func countBits(num int) int {
    count := 0
    for num > 0 {
        count += num % 2
        num >>= 1
    }
    return count
}

func canSortArray(nums []int) bool {
    n := len(nums)
    prev_bits := countBits(nums[0])
    maxx := 0
    prev := nums[0]
    for i := 1; i < n; i++ {
        bits := countBits(nums[i])
        if bits == prev_bits {
            if nums[i] < maxx {
                return false
            }
            prev = max(prev, nums[i])
            continue
        } else if nums[i] < prev {
            return false
        }

        maxx = prev
        prev = nums[i]
        prev_bits = bits
    }
    return true
}
