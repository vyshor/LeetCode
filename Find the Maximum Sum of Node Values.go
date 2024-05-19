func maximumValueSum(nums []int, k int, edges [][]int) int64 {
    msb := -1
    i := k
    for i > 0 {
        msb++
        i >>= 1
    }

    msb_count := 0
    maxx_msb := int64(1 << msb)
    mask := int64((1 << (msb+1))-1)
    var total, mask_total int64
    n := len(nums)
    k2 := int64(k)

    minn := mask << 1
    for _, num := range nums {
        num2 := int64(num)
        i := num2 & mask
        total += num2 ^ i
        if i < maxx_msb {
            i ^= k2
        } else {
            msb_count++
        }

        minn = min(minn, i - (i ^ k2))
        mask_total += i
    }

    non_msb_count := n - msb_count
    if non_msb_count % 2 == 1 {
        return total + mask_total - minn
    }
    return total + mask_total
}

