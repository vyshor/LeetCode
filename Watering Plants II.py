class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        n = len(plants)
        left, right = 0, n - 1
        capA, capB = capacityA, capacityB
        count = 0
        while left < right:
            if capA < plants[left]:
                count += 1
                capA = capacityA - plants[left]
            else:
                capA -= plants[left]
            left += 1

            if capB < plants[right]:
                count += 1
                capB = capacityB - plants[right]
            else:
                capB -= plants[right]
            right -= 1

        if left == right:
            count += int(plants[right] > max(capA, capB))

        return count

