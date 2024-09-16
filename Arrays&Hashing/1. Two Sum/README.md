1. Two Sum

- Link: https://leetcode.com/problems/two-sum/description/
- Difficulty: Easy
- Topics: Array, Hash map

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:

* 2 <= nums.length <= 10^4
* -10^9 <= nums[i] <= 10^9
* -10^9 <= target <= 10^9
* Only one valid answer exists


UMPIRE Method:

Understand

- Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
- Choose a “happy path” test input, different than the one provided, and a few edge case inputs.
- Verify that you and the interviewer are aligned on the expected inputs and outputs.

1. Can the nums array be empty?
2. Any requirement on time complexity?
3. Is the array sorted?
4. Will the numbers in the array duplicate?

Match 

- See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category

1. Sort: Will not help because we have to return the index of the elements
2. Hash map: Using a hash map to store elements of the array enables us to efficiently maintain the association between indices and values

Plan 

- Sketch visualizations and write pseudocode
- Walk through a high level implementation with an existing diagram

General Idea: Create a hash map to store index and number so that we can refer to the hash map for the index once we find the counterpart

1. Create a hash map
2. Iterate through the nums array
    - For each num, calculate the complement
    - If we see the complement in the hash map, return the current index and the complement's index
    - Add the current num and index to the hash map
    
Implement 

- Implement the solution (make sure to know what level of detail the interviewer wants)

See solution.py

Review

- Re-check that your algorithm solves the problem by running through important examples
- Go through it as if you are debugging it, assuming there is a bug

Evaluate 

- Finish by giving space and run-time complexity
- Discuss any pros and cons of the solution

Assume N represents the number of items in the array.
- Time complexity: O(N)
- Space complexity: O(N)
