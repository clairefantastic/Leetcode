75. Sort Colors

- Link: https://leetcode.com/problems/sort-colors/description/
- Difficulty: Medium
- Topics: Quick Sort, Bucket Sort

Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

Example 1:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Example 2:
Input: nums = [2,0,1]
Output: [0,1,2]

Constraints:

- n == nums.length
- 1 <= n <= 300
- nums[i] is either 0, 1, or 2

Follow up: Could you come up with a one-pass algorithm using only constant extra space?

UMPIRE Method:

Understand

- Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
- Choose a “happy path” test input, different than the one provided, and a few edge case inputs.
- Verify that you and the interviewer are aligned on the expected inputs and outputs.

1. Can the input be empty? (Yes)
2. Any requirement on time/space complexity? (O(n) in time and O(1) in space)

Match

- See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category

1. Bucket Sort
    - Pros: Great Time complexity (O(n))
    - Cons: Can only be used when the input is specific
2. Quick Sort

Plan

- Sketch visualizations and write pseudocode
- Walk through a high level implementation with an existing diagram

1. Bucket Sort: 
    - Declare a bucket array to store the number of times each value appears
    - Iterate through the nums array
    - Reset the nums array with the bucket array
2. Quick Sort:
    - Left pointer start from the beginning, right pointer start from the end
    - Iterate through the nums array (i)
    - While i <= right pointer, when encountering 0, swap with the value in the left pointer, left pointer increment 1, when encountering 2, swap with the value in the right pointer, right pointer decrement 1, (don't increment i for right swap)
    
Implement

- Implement the solution (make sure to know what level of detail the interviewer wants)

See solution.py

Review

- Re-check that your algorithm solves the problem by running through important examples
- Go through it as if you are debugging it, assuming there is a bug

Evaluate

- Finish by giving space and run-time complexity
- Discuss any pros and cons of the solution

1. Bucket Sort
Assume N elements in nums array
- Time Complexity: O(N)
- Space Complexity: O(1)

2. Quick Sort 
Assume N elements in nums array
- Time Complexity: O(N)
- Space Complexity: O(1)
