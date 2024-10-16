11. Container With Most Water

- Link: https://leetcode.com/problems/container-with-most-water/description/
- Difficulty: Medium
- Topics: Array, Two Pointer

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.


Example 1:

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 2:

Input: height = [1,1]
Output: 1

Constraints:

* n == height.length
* 2 <= n <= 10^5
* 0 <= height[i] <= 10^4


UMPIRE Method:

Understand

- Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
- Choose a “happy path” test input, different than the one provided, and a few edge case inputs.
- Verify that you and the interviewer are aligned on the expected inputs and outputs.

1. Can the input array be empty? (No, exactly one solution)
2. Any requirement on time complexity?
3. Is the array sorted? (No)

Match 

- See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category

1. Brute force: Try every single possible containers and find the maximum. It works but exceed time limit.
2. Pointers: Use two pointers, one from the left and the other from the right.

Plan 

- Sketch visualizations and write pseudocode
- Walk through a high level implementation with an existing diagram

General Idea: Begin by calculating the area formed by the outermost lines (Maximize the width first). To maximize it, we move the pointer of the shorter line inwards. Although this reduces width, the potential increase in height could surpass the width reduction, enhancing the overall area

1. Initialize the max area variable to keep track of the max area
2. Initialize the two pointers, left and right, where left starts from 0, and right starts from the end of the array
3. Calculate and keep track of the maximum area of the container
    - If left line is shorter or equal to the right line, move left by 1
    - If right line is shorter to the left line, move right by 1
    - Stop when left equal or exceed right
4. Return the max area
    
Implement 

- Implement the solution (make sure to know what level of detail the interviewer wants)

See solution.py

Review

- Re-check that your algorithm solves the problem by running through important examples
- Go through it as if you are debugging it, assuming there is a bug

Evaluate 

- Finish by giving space and run-time complexity
- Discuss any pros and cons of the solution

Assume N represents the number of numbers in the array.
- Time complexity: O(N)
- Space complexity: O(N)
