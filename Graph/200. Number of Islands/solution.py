class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        count = 0
        visit = set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        ROWS = len(grid)
        COLS = len(grid[0])

        def dfs(r, c):
            visit.add((r, c))
            for dr, dc in directions:
                newR, newC = r + dr, c + dc
                if min(newR, newC) >= 0 and newR < ROWS and newC < COLS and (newR, newC) not in visit and grid[newR][newC] == '1':
                    dfs(newR, newC)

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visit and grid[r][c] == '1':
                    count += 1
                    dfs(r, c)
            
        return count
