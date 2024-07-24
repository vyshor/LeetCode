func powInt(x, y int) int {
    return int(math.Pow(float64(x), float64(y)))
}

func convert(i int, mapping *[]int) int {
    m := *mapping
    if i == 0 {
        return m[i]
    }

    j := 0
    n := 0
    for i > 0 {
        j += m[i % 10] * powInt(10, n)
        n++
        i /= 10
    }
    return j
}

type Val struct {
    C int
    I int
    Num int
}

func sortJumbled(mapping []int, nums []int) []int {
    arr := make([]Val, 0)
    for i, num := range nums {
        arr = append(arr, Val{C: convert(num, &mapping), I:i, Num:num})
    }

    sort.Slice(arr, func (i, j int) bool {
        if arr[i].C == arr[j].C {
            return arr[i].I < arr[j].I
        }
        return arr[i].C < arr[j].C
    })

    ans := make([]int, 0)
    for _, p := range arr {
        ans = append(ans, p.Num)
    }
    return ans
}
