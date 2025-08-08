from typing import List

# Topic need to know for dealing with this kinda problem
"""
    1) Matrix / Grid Traversal
    2) Depth-First Search and Breath First Search
    3) Visited Matrix / Marking States
    4) Flood Fill (Reverse Simulation)
    5) Set intersection / Combining Results

"""



# DFS based

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        rows, cols = len(heights), len(heights[0])
        pacific = [[False] * cols for _ in range(rows)]
        atlantic = [[False] * cols for _ in range(rows)]

        def dfs(r, c, visited, prev_height):
            if (r < 0 or c < 0 or r >= rows or c >= cols or
                visited[r][c] or heights[r][c] < prev_height):
                return
            visited[r][c] = True
            directions = [(0,1), (1,0), (-1,0), (0,-1)]
            for dr, dc in directions:
                dfs(r + dr, c + dc, visited, heights[r][c])

        # Pacific: top and left
        for c in range(cols):
            dfs(0, c, pacific, heights[0][c])        # Top row
            dfs(rows - 1, c, atlantic, heights[rows - 1][c])  # Bottom row
        for r in range(rows):
            dfs(r, 0, pacific, heights[r][0])        # Left column
            dfs(r, cols - 1, atlantic, heights[r][cols - 1])  # Right column

        result = []
        for r in range(rows):
            for c in range(cols):
                if pacific[r][c] and atlantic[r][c]:
                    result.append([r, c])
        return result


# Need deep understanding

# BFS based
from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        rows, cols = len(heights), len(heights[0])
        pacific = [[False] * cols for _ in range(rows)]
        atlantic = [[False] * cols for _ in range(rows)]

        def dfs(r, c, visited, prev_height):
            if (r < 0 or c < 0 or r >= rows or c >= cols or
                visited[r][c] or heights[r][c] < prev_height):
                return
            visited[r][c] = True
            directions = [(0,1), (1,0), (-1,0), (0,-1)]
            for dr, dc in directions:
                dfs(r + dr, c + dc, visited, heights[r][c])

        # Pacific: top and left
        for c in range(cols):
            dfs(0, c, pacific, heights[0][c])        # Top row
            dfs(rows - 1, c, atlantic, heights[rows - 1][c])  # Bottom row
        for r in range(rows):
            dfs(r, 0, pacific, heights[r][0])        # Left column
            dfs(r, cols - 1, atlantic, heights[r][cols - 1])  # Right column

        result = []
        for r in range(rows):
            for c in range(cols):
                if pacific[r][c] and atlantic[r][c]:
                    result.append([r, c])
        return result
