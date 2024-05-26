class Solution:
    def checkRecord(self, s: str) -> bool:
        absent = 0
        late = 0
        for c in s:
            if c == "L":
                late += 1
                if late == 3:
                    return False
            else:
                late = 0
                absent += int(c == 'A')
        return absent <= 1
