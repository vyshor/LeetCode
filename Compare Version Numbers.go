func compareStr(v1, v2 []string, n int) int {
    for i := 0; i < n; i++ {
        v1i, _ := strconv.Atoi(v1[i])
        v2i, _ := strconv.Atoi(v2[i])
        if v1i == v2i {
            continue
        }

        if v1i < v2i {
            return -1
        } else if v2i < v1i {
            return 1
        }
    }

    return 0
}

func compareVersion(version1 string, version2 string) int {
    v1 := strings.Split(version1, ".")
    v2 := strings.Split(version2, ".")
    n := max(len(v1), len(v2))
    for len(v1) < n {
        v1 = append(v1, "0")
    }

    for len(v2) < n {
        v2 = append(v2, "0")
    }

    return compareStr(v1, v2, n)
}
