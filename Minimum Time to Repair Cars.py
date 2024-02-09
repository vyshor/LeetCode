class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        n = len(ranks)
        min_rank = min(ranks)
        lower, upper = 1, min_rank * cars * cars + 1
        ans = upper

        while lower < upper:
            mid = (upper + lower) // 2
            count = cars

            for rank in ranks:
                max_cars = math.floor(math.sqrt(mid / rank))
                count -= max_cars

            if count <= 0:
                ans = min(ans, mid)
                upper = mid
            else:
                lower = mid + 1

        return ans


