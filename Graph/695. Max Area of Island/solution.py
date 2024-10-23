class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        maxArea = 0

        def dfs(r, c, area):
            visit.add((r, c))
            area += 1

            for dr, dc in directions:
                newR = r + dr
                newC = c + dc
                if min(newR, newC) >= 0 and newR < ROWS and newC < COLS and (newR, newC) not in visit and grid[newR][newC] == 1:
                    area = dfs(newR, newC, area)
            
            return area
            
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visit and grid[r][c] == 1:
                    area = dfs(r, c, 0)
                    maxArea = max(area, maxArea)

        return maxArea 
