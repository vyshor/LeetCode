func passThePillow(n int, time int) int {
    turn := 2*n-2
    time %= turn
    if time >= n {
        return 2*n - time - 1
    }
    return time+1
}

