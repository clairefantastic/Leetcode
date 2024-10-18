90. Subsets ii

- Link: https://leetcode.com/problems/subsets-ii/description/
- Difficulty: Medium 
- Topics: Array, Backtracking

Given an integer array nums that may contain duplicates, return all possible 
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.


Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

Example 2:

Input: nums = [0]
Output: [[],[0]]

Constraints:

- 1 <= nums.length <= 10
- -10 <= nums[i] <= 10


UMPIRE Method:

Understand

- Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
- Choose a “happy path” test input, different than the one provided, and a few edge case inputs.
- Verify that you and the interviewer are aligned on the expected inputs and outputs.

1. Can the input be empty? (Yes)
2. Any requirement on time/space complexity? 
3. Is the input array assumed sorted? (No)

Match

- See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category

1. Backtracking: In the backtracking function, add a condition to skip over duplicate elements. After choosing an element to be included in the current subset, if the next element in the array is same as the current one, skip it to avoid creating duplicate subsets.
2. Sorting: This step is crucial to ensure that duplicates are adjacent, making it easier to skip over duplicates when building subsets.

Plan

- Sketch visualizations and write pseudocode
- Walk through a high level implementation with an existing diagram

General Idea: in the while loop inside the backtrack function, there is check to skip the current element if it is same as the previous one

1. Initialize an empty result list
2. Sort the numbers 
3. Backtrack function (Takes in two parameters, i represents the current index we are in nums and subset represents the current subset we created): 
    - If i is equal to the nums length, we append the copy of this subset array to the result and return
    - Append the nums[i] (current element)
    - backtrack(i + 1, subset)
    - Pop the element from the subset to explore other possibilities
    - While i + 1 is in bound and is same as the previous element (i), increase i until it is different from the previous element 
    - backtrack(i + 1, subset)
4. Call the backtrack function
5. Return the result
    
Implement

- Implement the solution (make sure to know what level of detail the interviewer wants)

See solution.py

Review

- Re-check that your algorithm solves the problem by running through important examples
- Go through it as if you are debugging it, assuming there is a bug

Evaluate

- Finish by giving space and run-time complexity
- Discuss any pros and cons of the solution

Assume N is the number of elements in the input array.

- Time Complexity: O(N * 2^N)
- Space Complexity: O(N * 2^N)
