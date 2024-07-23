func frequencySort(nums []int) []int {
    counter := make(map[int]int)
    for _, num := range nums {
        counter[num] += 1
    }

    sort.Slice(nums, func (i, j int) bool {
        if counter[nums[i]] == counter[nums[j]] {
            return nums[i] > nums[j]
        }
        return counter[nums[i]] < counter[nums[j]]
    })
    return nums
}
