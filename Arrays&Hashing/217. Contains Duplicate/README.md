217. Contain Duplicates

- Link: https://leetcode.com/problems/contains-duplicate/description/
- Difficulty: Easy
- Topics: Array, Hash map

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:

Input: nums = [1,2,3,1]
Output: true

Explanation:
The element 1 occurs at the indices 0 and 3.

Example 2:

Input: nums = [1,2,3,4]
Output: false

Explanation:
All elements are distinct.

Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

Constraints:

* 1 <= nums.length <= 10^5
* -10^9 <= nums[i] <= 10^9


UMPIRE Method:

Understand

- Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
- Choose a “happy path” test input, different than the one provided, and a few edge case inputs.
- Verify that you and the interviewer are aligned on the expected inputs and outputs.

1. Can the nums array be empty?
2. Any requirement on time complexity?
3. Is the array sorted?

Match 

- See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category

1. Set: As we iterate through the array, we can store each number in a set. If the number is already in the Set, return True. Otherwise we reach the end and return False.

Plan 

- Sketch visualizations and write pseudocode
- Walk through a high level implementation with an existing diagram

General Idea: Create a Set to store numbers. If the number is already in the Set, then return True. Otherwise we reach the end of the array and return False.

1. Create a Set
2. Iterate through the nums array
    - If number is already in set return True
    - Else store number in set
3. Return False if we have reached the end of the list without duplicate
    
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

