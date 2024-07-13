type Node struct {
    pos int
    i int
    h int
    dir bool
}

func survivedRobotsHealths(positions []int, healths []int, directions string) []int {
    arr := make([]Node, 0)
    n := len(positions)
    for i := range n {
        arr = append(arr, Node{positions[i], i, healths[i], directions[i] == 'R'})
    }

    sort.Slice(arr, func(i, j int) bool {
        return arr[i].pos < arr[j].pos
    })

    stack := make([][]int, 0)
    ans := make([]int, n)
    for i := range n {
        j, h, is_right := arr[i].i, arr[i].h, arr[i].dir
        if is_right {
            stack = append(stack, []int{j, h})
        } else {
            for len(stack) > 0 {
                if stack[len(stack)-1][1] == h {
                    h = 0
                    stack = stack[:len(stack)-1]
                    break
                } else if stack[len(stack)-1][1] > h {
                    h = 0
                    stack[len(stack)-1][1]--
                    break
                } else {
                    stack = stack[:len(stack)-1]
                    h--
                }
            }

            if h > 0 {
                ans[j] = h
            }
        }
    }

    for _, jh := range stack {
        ans[jh[0]] = jh[1]
    }
    truncated_ans := make([]int, 0)
    for _, h := range ans {
        if h != 0 {
            truncated_ans = append(truncated_ans, h)
        }
    }
    return truncated_ans
}
