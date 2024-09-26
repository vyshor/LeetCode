type MyCalendar struct {
    Arr [][]int
}


func Constructor() MyCalendar {
    return MyCalendar{}
}


func (this *MyCalendar) Book(start int, end int) bool {
    p := []int{start, end}
    i := sort.Search(len(this.Arr), func(i int) bool {
        if this.Arr[i][0] > start {
            return true
        } else if this.Arr[i][0] > start {
            return false
        }
        return this.Arr[i][1] >= end
        })
    if i != 0 {
        i2 := i-1
        if this.Arr[i2][1] > start {
            return false
        }
    }

    if i != len(this.Arr) {
        if this.Arr[i][0] < end {
            return false
        }
    }

    this.Arr = slices.Insert(this.Arr, i, p)
    return true
}


/**
 * Your MyCalendar object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Book(start,end);
 */
