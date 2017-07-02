class Solution(object):
    def uniquePathsWithObstacles(self, g):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(g)
        n = len(g[0])
        a = []
        for i in range(m):
            a.append([0] * n)
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if g[i][j] == 1:
                    g[i][j] = 0
                else:
                    if i == m - 1 and j == n - 1:
                        a[i][j] = 1
                    else:
                        if i + 1 < m:
                            a[i][j] += a[i + 1][j]
                        if j + 1 < n:
                            a[i][j] += a[i][j + 1]

        return a[0][0]
