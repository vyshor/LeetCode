class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        counter = Counter(nums)
        grid = []
        for num, count in counter.items():
            for i in range(count):
                if i == len(grid):
                    grid.append([num])
                else:
                    grid[i].append(num)
        return grid
