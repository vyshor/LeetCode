class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        summ = 0
        n = len(seats)
        for i in range(n):
            summ += abs(seats[i]-students[i])
        return summ
