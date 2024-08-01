27. Remove Element

Link: https://leetcode.com/problems/remove-element/description/
Difficulty: Easy
Topics: Array

Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

- Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
- Return k.

Example 1:

Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).

Example 2:

Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).


Constraints:

0 <= nums.length <= 100
0 <= nums[i] <= 50
0 <= val <= 100

UMPIRE Method:

Understand

- Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
- Choose a “happy path” test input, different than the one provided, and a few edge case inputs.
- Verify that you and the interviewer are aligned on the expected inputs and outputs.

1. Can the nums array be empty?
2. Any requirement on time complexity?

Match

- See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category

Two pointers: The left pointer enable us to know where our next element which is not equal to val should be place in, and also tell us how many values which are not equal to val are there in the array. The right pointer will enable us to throw all the elements which equal to val to the end of the array.

Plan

- Sketch visualizations and write pseudocode
- Walk through a high level implementation with an existing diagram

1. Define a left pointer (from index 0) and a right pointer (from the last index)
2. Iterate through the array (When the left pointer is less than the right pointer)
    - If an element equals to val, swap the elements where the left and right pointer is, and the right pointer shifts left
    - If an element doesn't equal to val, the left pointer shifts right
3. Return the right pointer, the nums array are as the required form

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
- Space complexity: O(1)
