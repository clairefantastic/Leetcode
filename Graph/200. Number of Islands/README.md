200. Number of Islands

- Link: https://leetcode.com/problems/number-of-islands/description/
- Difficulty: Medium
- Topics: Graph, Matrix, DFS, BFS

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.


Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

Constraints:

* m == grid.length
* n == grid[i].length
* 1 <= m, n <= 300
* grid[i][j] is '0' or '1'.


UMPIRE Method:

Understand

- Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
- Choose a “happy path” test input, different than the one provided, and a few edge case inputs.
- Verify that you and the interviewer are aligned on the expected inputs and outputs.

1. Can the input grid be empty? (No)
2. Any requirement on time/space complexity? (O(m * n) in time and O(1) in space)
3. Can the islands have irregular shapes? (Yes)
4. Do diagonal connections between islands count towards forming islands? (No)

Match 

- See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category

1. DFS:
    - Traversal: Iterate over each cell in the grid. When a '1' is found, increment the island count and then traverse its neighboring land cells to mark the entire island
    - Marking Visited Cells: To avoid counting the same land twice, we can mark the visited land cells by using a separate visited structure
    - Recursion: Implement DFS recursively. When a land cell is found, call DFS for its four adjacent
    - Edge Handling: Ensure that the DFS doesn't go out of bounds of the grid and only processes land cells
    - Complexity: Time complexity would be O(m*n) where m is the number of rows and n is the number of columns, since each cell is processed once. The space complexity depends on the recursion depth, which can be up to O(mn) in the worst case
2. BFS: 
    - Queue-based Implementation: Use a queue to implement BFS. When a land cell is found, add it to the queue and process its neighbors iteratively
    - Marking and Processing: Similar to DFS, mark cells as visited. Process cells in the queue and add their unvisited land neighbors to the queue
    - Iterative approach: BFS is naturally iterative, which avoids the potential stack overflow issue of DFS in large grids
    - Complexity: Time complexity remains O(m*n) as all cells are processed once. Then space complexity is O(min(m , n)) in the worst case, as in the worst case, the queue will have all cells from the largest row or column

Plan 

- Sketch visualizations and write pseudocode
- Walk through a high level implementation with an existing diagram

General Idea: Use a DFS approach to explore the grid and identify the islands; we can save the islands we have visted 

1. Initialize Count, Directions, Visit: We start by initializing a count to 0, which will hold our total number of islands. We also set up a direction array to easily check adjacent cells. Furthermore, also declare a set visit to record the cells visited
2, Iterate Over the Grid: We loop through each cell in the grid. For each cell, if it is land('1') and not in visit, we increment the count of island because we found a new island and then call DFS recursively to explore connected land cells. 
3. DFS function: Take in two parameters r and c representing the current row and column. Add it the visit set. Loop through the neighboring directions and check if the neighbors can be visited, if yes, call recursive DFS. This process ensures we will not count them as new islands again when the next time we encounter them.
4. Marking Island Territory: The DFS will continue to spread from each land cell to its adjacent land cells, marking each as visited. This process ensures that we count all connected '1' as a single island
5. Complete the Search: Once DFS is complete for an island, the search continues from the next unvisited land cell in the grid. Each new unvisited land cell starts a new DFS adn potentially identifies a new island
6. Return the Count

Implement 

- Implement the solution (make sure to know what level of detail the interviewer wants)

See solution.py

Review

- Re-check that your algorithm solves the problem by running through important examples
- Go through it as if you are debugging it, assuming there is a bug

Evaluate 

- Finish by giving space and run-time complexity
- Discuss any pros and cons of the solution

Assume the grid has M rows and N columns
- Time complexity: O(M * N)
- Space complexity: O(M * N)

