func wonderfulSubstrings(word string) int64 {
    counter := make(map[int]int64)
    counter[0] = 1
    var current int
    var count int64
    for _, c := range word {
        shift := 1<<((int)(c-'a'))
        current ^= shift

        if val, ok := counter[current]; ok {
            count += val
            counter[current]++
        } else {
            counter[current] = 1
        }

        for i := 0; i < 10; i++ {
            new_mask := current ^ (1 << i)
            if val, ok := counter[new_mask]; ok {
                count += val
            }
        }
    }

    return count
}

