type Pair struct {
    num int
    pos int
}


func subarraysWithKDistinct(nums []int, k int) int {
    last_pos := make(map[int]int)
    n := len(nums)
    count := 0
    var left, right int
    q := make([]Pair, 0)
    i := 0

    for right < n {
        num := nums[right]
        last_pos[num] = right
        q = append(q, Pair{num:num , pos:right})

        for len(last_pos) > k || last_pos[q[i].num] != q[i].pos {
            num = q[i].num
            pos := q[i].pos
            if pos == last_pos[num] {
                left = last_pos[num]+1
                delete(last_pos, num)
            }
            i++
        }

        if len(last_pos) == k {
            count += q[i].pos - left + 1
        }

        right++
    }

    return count
}
