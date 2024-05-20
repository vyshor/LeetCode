type StockSpanner struct {
    val []int
    count []int

    n int
}


func Constructor() StockSpanner {
    return StockSpanner{}
}


func (this *StockSpanner) Next(price int) int {
    total := 1
    for this.n > 0 && this.val[this.n-1] <= price {
        this.n--
        total += this.count[this.n]
        this.val = this.val[:this.n]
        this.count = this.count[:this.n]
    }
    this.val = append(this.val, price)
    this.count = append(this.count, total)
    this.n++
    return total
}


/**
 * Your StockSpanner object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Next(price);
 */
