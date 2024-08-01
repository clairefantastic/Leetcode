26. Remove Duplicates from Sorted Array

- Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
- Difficulty: Easy
- Topics: Array

Given an integer array nums sorted in non-decreasing (the successive element is greater than or equal to its previous element) order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

- Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
- Return k.


Example 1:

Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

Example 2:

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

Constraints:

* 1 <= nums.length <= 3 * 10^4
* -100 <= nums[i] <= 100
* nums is sorted in non-decreasing order.


UMPIRE Method:

Understand

- Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
- Choose a “happy path” test input, different than the one provided, and a few edge case inputs.
- Verify that you and the interviewer are aligned on the expected inputs and outputs.

1. Can the nums array be empty?
2. Any requirement on time complexity?

Match 

- See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category

1. Two pointers: The left pointer enable us to know where our next unique element should be place in, and also tell us how many unique value are there in the array. The right pointer will scan through the array and find the unique element. 

Plan 

- Sketch visualizations and write pseudocode
- Walk through a high level implementation with an existing diagram

1. Define a left pointer and a right pointer
2. Iterate through the array (Shifting the right pointer)
    - If we find an element different from the previous element, assign this element to the place the left pointer is, and the left pointer should shift right
3. Return the left pointer, the nums array are as the required form
    
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
