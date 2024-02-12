type Pair struct {
    count int
    path []int
}

func largestDivisibleSubset(nums []int) []int {
    slices.Sort(nums)
    dp := make(map[int]Pair)
    maxx := 0
    var ans_key int
    for _, num := range nums {
        count := 1;
        prev_num := -1;
        for key, pair := range dp {
            if (num % key == 0 && pair.count+1 > count) {
                count = pair.count+1
                prev_num = key
            }
        }

        path := make([]int, 0)
        if prev_num != -1 {
            path = make([]int, len(dp[prev_num].path))
            copy(path, dp[prev_num].path)
        }
        path = append(path, num)
        dp[num] = Pair {count: count, path: path}

        if count > maxx {
            maxx = count
            ans_key = num
        }
    }
    return dp[ans_key].path
}
