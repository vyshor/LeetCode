class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        def getCount(state):
            return max((int(state & 0x0011 == 0x0011) + int(state & 0x1100 == 0x1100)), int(state & 0x0110 == 0x0110))

        states = {}
        count = n*2
        for (row, seat) in reservedSeats:
            prev_state = states.get(row, 0x1111)
            old_count = getCount(prev_state)
            if old_count == 0:
                continue

            new_state = prev_state

            if 4 <= seat <= 5:
                new_state &= 0x1011

            elif 6 <= seat <= 7:
                new_state &= 0x1101

            elif 2 <= seat <= 3:
                new_state &= 0x0111

            elif 8 <= seat <= 9:
                new_state &= 0x1110

            if new_state == prev_state:
                continue

            new_count = getCount(new_state)
            count -= old_count - new_count
            states[row] = new_state
        return count
