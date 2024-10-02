type CustomStack struct {
    N int
    Arr []int
}


func Constructor(maxSize int) CustomStack {
    return CustomStack{N: maxSize, Arr: make([]int, 0)}
}


func (this *CustomStack) Push(x int)  {
    if len(this.Arr) < this.N {
        this.Arr = append(this.Arr, x)
    }
}


func (this *CustomStack) Pop() int {
    if len(this.Arr) > 0 {
        val := this.Arr[len(this.Arr)-1]
        this.Arr = this.Arr[:len(this.Arr)-1]
        return val
    }
    return -1
}


func (this *CustomStack) Increment(k int, val int)  {
    for i := 0; i < min(k, len(this.Arr)); i++ {
        this.Arr[i] += val
    }
}


/**
 * Your CustomStack object will be instantiated and called as such:
 * obj := Constructor(maxSize);
 * obj.Push(x);
 * param_2 := obj.Pop();
 * obj.Increment(k,val);
 */
