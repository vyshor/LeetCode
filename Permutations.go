import (
    "fmt"
    "sync"
    "sync/atomic"
)

type State struct {
    current []int
    remaining []int
}

func permute(nums []int) [][]int {

    n := len(nums)
    q := make(chan State, 1000)
    final := make(chan []int)
    done := make(chan bool)
    finalDone := make(chan bool)
    ans := make([][]int, 0)
    running := int32(1)

    defer close(q)
    defer close(final)
    defer close(finalDone)
    defer close(done)

    go func() {
        for {
            select {
                case <- finalDone:
                    return
                case arr := <- final:
                    ans = append(ans, arr)
            }
        }
    }()

	var wg sync.WaitGroup

    consumerCount := n * 100
    wg.Add(consumerCount)

    for i := 0; i < consumerCount; i++ {

        go func() {
            defer wg.Done()

            for {
                select {
                    case state := <- q:
                        consume(state, q, final, &running)
                    case <- done:
                        return
                }
            }
        }()
    }

    q <- State{
        current: []int{},
        remaining: nums,
    }

    for (running != 0) {}

    for i := 0; i < consumerCount; i++ {
        done <- true
    }

    return ans
}

func consume(state State, q chan State, final chan []int, running *int32) {

    current := state.current
    remaining := state.remaining

    if len(remaining) == 0 {
        final <- current

        go func() {
            atomic.AddInt32(running, -1)
        }()

        return
    }

    atomic.AddInt32(running, int32(len(remaining) - 1))
    for i, r := range remaining {
        newCurrent := make([]int, len(current))
        copy(newCurrent, current)

        newRemaining := make([]int, len(remaining))
        copy(newRemaining, remaining)

        q <- State{
            current: append(newCurrent, r),
            remaining: append(newRemaining[:i], newRemaining[i+1:]...),
        }
    }
}