78. Subsets

- Link: https://leetcode.com/problems/subsets/description/
- Difficulty: Medium
- Topics: Array, Backtracking

Given an integer array nums of unique elements, return all possible 
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:

Input: nums = [0]
Output: [[],[0]]

Constraints:

- 1 <= nums.length <= 10
- -10 <= nums[i] <= 10
- All the numbers of nums are unique.

UMPIRE Method:

Understand

- Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
- Choose a “happy path” test input, different than the one provided, and a few edge case inputs.
- Verify that you and the interviewer are aligned on the expected inputs and outputs.

1. Any requirement on time/space complexity? 
2. Can the input be empty? What should I return for an empty array? (Yes, return an empty array)
3. Is the input array assumed to be sorted? (No)

Match

- See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category

1. Backtracking: Whenever we have a problem where we need to generate all combinations/permutations of some group of letters/numbers, the first thought we should have is backtracking. Backtracking algorithms can often keep the space complexity linear with the input size. The strategy accepts the cases which satisfy conditions and reject the others. We basically loop over every element in our input nums, and we recursively call the method to generate subsets corresponding to that element in the next line and then we remove that element since we are done with it, and we add it to our subsets array.

Plan

- Sketch visualizations and write pseudocode
- Walk through a high level implementation with an existing diagram

General Idea:
- Use a recursive dfs function, named dfs, to build subsets recursively. The function dfs takes one parameter: i, which represents the current index in the array nums. The method begins with an empty subset and explores all possible elements to be included in the current subset. 

1. Initialize an Empty Result List: The method subsets initializes an empty list res to store all results. 
2. Initialize a Subset List
3. Recursively dfs Function: When i is greater or equal to the length of nums, the result array append the current subset
4. Building Subsets recursively:
    - For each index i in the range from start to the end of the array, the element nums[i] is appended to the current subset path.
    - Recursively call the next index i+1
4. Backtracking to Explore Other Possibilities:
    - After the recursive call, subset.pop() is executed, which removes the last element added to the subset. This step is crucial as it undoes the last addition, allowing the function to backtrack and explore other subset combinations by including different elements in subsequent recursion.
5. Complete Exploration: The process continues until the i is greater than or equal to len(nums)
6. Returning the Result: Once all recursive calls are complete and all possible subsets have been explored and added to res, return the result array
    
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

Time Complexity: O(2^N), at each step, the algorithm explores two possibilities for each element – either including it in the current subset or not.
Space Complexity: O(h), where h represents the maximum depth of the recursion stack if we exclude the space required for the output list
