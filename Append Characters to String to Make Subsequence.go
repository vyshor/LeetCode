func appendCharacters(s string, t string) int {
    var s1, t1 int
    sn, tn := len(s), len(t)
    for t1 < tn {
        for s1 < sn {
            if s[s1] == t[t1] {
                s1++
                t1++
                break
            } else {
                s1++
            }
        }

        if s1 == sn {
            return tn - t1
        }
    }
    return 0
}
