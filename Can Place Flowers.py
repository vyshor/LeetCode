class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        bedsize = len(flowerbed)

        if n == 0:
            return True

        prev = flowerbed[0]
        for i in range(bedsize):
            prev = i - 1 < 0 or not flowerbed[i - 1]
            next = i + 1 >= bedsize or not flowerbed[i + 1]
            if flowerbed[i] == 0 and prev and next:
                flowerbed[i] = 1
                n -= 1

                if n == 0:
                    return True
        return False