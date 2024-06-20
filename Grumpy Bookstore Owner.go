func maxSatisfied(customers []int, grumpy []int, minutes int) int {
    n := len(customers)
    arr := make([]int, n)
    total := 0
    summ := 0
    for i := 0; i < n; i++ {
        if grumpy[i] == 0 {
            total += customers[i]
        }
        arr[i] = customers[i] * grumpy[i]
        if i < minutes-1 {
            summ += arr[i]
        }
    }

    maxx := summ
    left, right := 0, minutes-1
    for right < n {
        summ += arr[right]
        maxx = max(maxx, summ)
        summ -= arr[left]
        right++
        left++
    }
    return total + maxx
}

