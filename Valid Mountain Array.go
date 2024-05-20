func validMountainArray(arr []int) bool {
    n := len(arr)
    if n < 3 {
        return false
    }

    i := 0
    j := n-1
    for i < j && arr[i] < arr[i+1] {
        i++
    }

    for i < j && arr[j-1] > arr[j] {
        j--
    }

    return i == j && j != n-1 && i != 0
}

