func combinationSum2(candidates []int, target int) [][]int {
    counter := make(map[int]int)
    row := make([]int, 0)
    for _, num := range candidates {
        counter[num]++
        if counter[num] == 1 {
            row = append(row, num)
        }
    }

    total := target
    n := len(row)
    ans := make([][]int, 0)
    curr := make([]int, 0)

    var explore func(int)
    explore = func(i int) {
        if i == n {
            return
        }

        num := row[i]
        for j := 0; j < counter[num]+1; j++ {
            total -= num*j;
            if total < 0 {
                total += num*j
                continue
            }

            for k := 0; k < j; k++ {
                curr = append(curr, num)
            }

            if total == 0 {
                dup := append([]int{}, curr...)
                ans = append(ans, dup)
                total += num * j
                curr = curr[:len(curr)-j]
                continue
            }

            explore(i+1)
            curr = curr[:len(curr)-j]
            total += num * j
        }
    }
    explore(0)
    return ans
}
