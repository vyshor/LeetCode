func dividePlayers(skill []int) int64 {
    n := len(skill)
    if n % 2 == 1 {
        return -1
    }

    sort.Ints(skill)
    avg := skill[0] + skill[n-1]
    i := 0
    j := n-1
    chemistry := int64(0)
    for i < j {
        if skill[i] + skill[j] != avg {
            return -1
        }
        chemistry += int64(skill[i]) * int64(skill[j])
        i++
        j--
    }
    return chemistry
}
