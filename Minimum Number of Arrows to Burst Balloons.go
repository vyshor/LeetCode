func findMinArrowShots(points [][]int) int {
    sort.Slice(points, func(i, j int) bool {
		return points[i][1] < points[j][1]
	})
    var count, prev int
    for _, point := range points {
        if prev >= point[0] && count != 0 {
            continue
        }

        count++
        prev = point[1]
    }
    return count
}
