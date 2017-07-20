class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        r = 0
        rows = len(grid)
        cols = len(grid[0])
        n = sum(reduce(lambda a, b: a + b, grid))
        for i in range(rows):
            for j in range(cols - 1):
                if grid[i][j] and grid[i][j+1]:
                    r += 1

        for i in range(rows - 1):
            for j in range(cols):
                if grid[i][j] and grid[i+1][j]:
                    r += 1

        return 4 * n - 2 * r
