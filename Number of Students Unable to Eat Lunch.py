class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        n = len(sandwiches)
        n1, n2 = sum(students), sum(sandwiches)
        if n1==n2:
            return 0

        what = int(n1-n2 > 0)
        if what == 0:
            count = n - n2
            other_count = n1
        else:
            count = n2
            other_count = n - n1

        for i, s in enumerate(sandwiches):
            if s == what:
                if count > 0:
                    count -= 1
                else:
                    return n-i
            else:
                if other_count > 0:
                    other_count -= 1
                else:
                    return n-i
        return 0
