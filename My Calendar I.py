class MyCalendar:

    def __init__(self):
        self.bookings = []

    def book(self, start: int, end: int) -> bool:
        new_book = (start, end)
        i = bisect.bisect_left(self.bookings, new_book)
        if i != 0:
            prev_booking = self.bookings[i - 1]
            if prev_booking[1] > start:
                return False

        if i != len(self.bookings):
            nxt_booking = self.bookings[i]
            if nxt_booking[0] < end:
                return False
        # print(new_book, self.bookings)
        self.bookings.insert(i, new_book)
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
