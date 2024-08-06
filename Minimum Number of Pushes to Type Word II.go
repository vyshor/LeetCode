func minimumPushes(word string) int {
    counter := make(map[rune]int)
    for _, c := range word {
        counter[c]++
    }
    q := make([]int, 0)
    for _, v := range counter {
        q = append(q, -v)
    }
    sort.Ints(q)
    pushes := 0
    num_pad := 0
    rotation := 1
    for _, count := range q {
        pushes += -count * rotation
        num_pad++
        if num_pad == 8 {
            rotation++
            num_pad = 0
        }
    }
    return pushes
}
