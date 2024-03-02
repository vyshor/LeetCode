func maxNumberOfFamilies(n int, reservedSeats [][]int) int {
    getCount := func(state int) int {
        left := state & 0b0011 == 0b0011
        right := state & 0b1100 == 0b1100
        mid := state & 0b0110 == 0b0110

        if left && right {
            return 2
        } else {
            if left || right || mid {
                return 1
            } else{
                return 0
            }
        }
    }

    states := make(map[int]int)
    count := n*2
    for _, reservedSeat := range reservedSeats {
        row := reservedSeat[0]
        seat := reservedSeat[1]

        prev_state := 0b1111
        if state, ok := states[row]; ok {
            prev_state = state
        }

        old_count := getCount(prev_state)
        if old_count == 0 {
            continue
        }

        new_state := prev_state
        switch seat {
            case 2, 3:
            new_state &= 0b0111

            case 4, 5:
            new_state &= 0b1011

            case 6, 7:
            new_state &= 0b1101

            case 8, 9:
            new_state &= 0b1110

            default:
            continue
        }

        if new_state == prev_state {
            continue
        }

        new_count := getCount(new_state)
        count -= old_count - new_count
        states[row] = new_state
    }

    return count
}
