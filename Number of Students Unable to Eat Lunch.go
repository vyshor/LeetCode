func sum(a []int) int {
    var total int
    for _, i := range a {
        total += i
    }
    return total
}

func countStudents(students []int, sandwiches []int) int {
    n := len(sandwiches)
    n1 := sum(students)
    n2 := sum(sandwiches)
    if n1==n2 {
        return 0
    }

    var what int
    if n1-n2 > 0 {
        what = 1
    }

    var count, other_count int
    if what == 0 {
        count = n-n2
        other_count = n1
    } else {
        count = n2
        other_count = n - n1
    }

    for i, s := range sandwiches {
        if s == what {
            if count > 0 {
                count--
            } else {
                return n-i
            }
        } else {
            if other_count > 0 {
                other_count--
            } else {
                return n-i
            }
        }
    }
    return 0
}
