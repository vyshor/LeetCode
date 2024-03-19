class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        def convertTime(s):
            h, m = s.split(":")
            return int(h) * 60 + int(m)

        first_start = convertTime(event1[0])
        first_end = convertTime(event1[1])

        second_start = convertTime(event2[0])
        second_end = convertTime(event2[1])
        if first_start < second_start:
            return first_end >= second_start
        else:
            return second_end >= first_start

