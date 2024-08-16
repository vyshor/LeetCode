func maxDistance(arrays [][]int) int {
    INT_MIN := -10000
    INT_MAX := 10000

    minn0 := INT_MAX
    minn1 := INT_MAX
    maxx0 := INT_MIN
    maxx1 := INT_MIN
    var i0, j0 int

    for i, arr := range arrays {
        if arr[0] < minn0 {
            minn0, minn1 = arr[0], minn0
            i0 = i
        } else if arr[0] < minn1 {
            minn1 = arr[0]
        }

        m := len(arr)-1
        if arr[m] > maxx0 {
            maxx0, maxx1 = arr[m], maxx0
            j0 = i
        } else if arr[m] > maxx1 {
            maxx1 = arr[m]
        }
    }

    if i0 == j0 {
        return max(maxx0-minn1, maxx1-minn0)
    }
    return maxx0 - minn0
}
