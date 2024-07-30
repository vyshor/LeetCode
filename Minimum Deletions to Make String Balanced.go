func get(b bool) int {
    if b {
        return 1
    }
    return 0
}

func minimumDeletions(s string) int {
    state_a, state_b := 0, 0
    for _, c := range s {
        state_b = min(state_a, state_b) + get(c == 'a')
        state_a += get(c == 'b')
    }
    return min(state_a, state_b)
}
