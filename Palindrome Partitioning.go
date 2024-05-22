func partition(s string) [][]string {
    j := 0
    substring := make([]string, 0)
    for _, c := range s {
        substring = append(substring, string(c))
    }

    arr := [][]string{
        substring,
    }
    seen := make(map[string]interface{})

    var explore func([]string)
    explore = func(arr2 []string) {
        n := len(arr2)
        for i := 0; i < n-1; i++ {
            if arr2[i] == arr2[i+1] {
                arr3 := append([]string{}, arr2[:i]...)
                arr3 = append(arr3, arr2[i] + arr2[i+1])
                arr3 = append(arr3, arr2[i+2:]...)
                key := strings.Join(arr3, "-")
                if _, ok := seen[key]; !ok {
                    seen[key] = nil
                    arr = append(arr, arr3)
                }
            }
        }


        for i := 0; i < n-2; i++ {
            if arr2[i] == arr2[i+2] {
                arr3 := append([]string{}, arr2[:i]...)
                arr3 = append(arr3, arr2[i] + arr2[i+1] + arr2[i+2])
                arr3 = append(arr3, arr2[i+3:]...)
                key := strings.Join(arr3, "-")
                if _, ok := seen[key]; !ok {
                    seen[key] = nil
                    arr = append(arr, arr3)
                }
            }
        }
    }

    for j < len(arr) {
        explore(arr[j])
        j++
    }
    return arr
}
