class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        if jug1Capacity + jug2Capacity < targetCapacity:
            return False

        def gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a

        return targetCapacity % gcd(jug1Capacity, jug2Capacity) == 0
