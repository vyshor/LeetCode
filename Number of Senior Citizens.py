class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for detail in details:
            count += bool(int(detail[11] + detail[12]) > 60)
        return count
