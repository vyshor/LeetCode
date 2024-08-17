func smallestDistancePair(nums []int, k int) int {
    counter := make(map[int]int)
    keys := make([]int, 0)
    for _, num := range nums {
        if counter[num] == 0 {
            keys = append(keys, num)
        }
        counter[num]++
    }
    n := len(keys)
    sort.Ints(keys)

    for i := 0; i < n; i++ {
        if counter[keys[i]] > 1 {
            k -= counter[keys[i]] * (counter[keys[i]]-1) / 2
        }
    }

    if k <= 0 {
        return 0
    }

    check := func(window int) bool {
        left := 0
        limit := keys[left] + window
        i := left + 1
        count := 0
        for i < n && keys[i] <= limit {
            count += counter[keys[i]]
            i++
        }
        total := counter[keys[left]] * count
        for left < n-1 {
            if k <= total {
                return true
            }

            left++
            count -= counter[keys[left]]
            limit = keys[left] + window
            for i < n && keys[i] <= limit {
                count +=counter[keys[i]]
                i++
            }
            total += counter[keys[left]] * count
        }
        return k <= total
    }

    minn, maxx := 1, keys[n-1] - keys[0]
    for minn < maxx {
        mid := (minn + maxx) / 2
        left_side := check(mid)
        if left_side {
            maxx = mid
        } else {
            minn = mid+1
        }
    }
    return minn
}
