func bestClosingTime(customers string) int {
    var opened, closed, j int
    for i, c := range customers {
        var coming int
        if c == 'Y' {
            coming += 1
        }
        closed += coming
        if opened + coming < closed {
            closed = opened + coming
            j = i
        }
        opened += 1 ^ coming
    }
    if opened < closed {
        return len(customers)
    }
    return j
}

