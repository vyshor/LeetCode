func longestSquareStreak(nums []int) int {
    terms := make(map[int]int)
    nums2 := make([]int, 0)
    parents := make([]int, 0)
    counts := make([]int, 0)
    maxx := 1
    j := 0

    for _, num := range nums {
        if _, ok := terms[num]; !ok {
            terms[num] = j
            nums2 = append(nums2, num)
            parents = append(parents, j)
            j++
            counts = append(counts, 1)
        }
    }

    var find func(i int)int
    var union func(i, j int)

    find = func(i int) int {
        if parents[i] != i {
            return find(parents[i])
        }
        return i
    }

    union = func(i, j int) {
        parent_i := find(i)
        parent_j := find(j)
        if parent_i != parent_j {
            parents[parent_i] = parent_j
            counts[parent_j] += counts[parent_i]
            maxx = max(maxx, counts[parent_j])
        }
    }

    for i, num := range nums2 {
        if num >= 317 {
            continue
        }

        nxt := num * num
        if val, ok := terms[nxt]; ok {
            union(i, val)
        }
    }

    if maxx < 2 {
        return -1
    }
    return maxx
}
