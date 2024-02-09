class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        cap = capacity
        ans = 0
        for i, p in enumerate(plants):
            ans += 1
            if cap < p:
                ans += 2*i
                cap = capacity - p
            else:
                cap -= p
        return ans
