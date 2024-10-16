15. Three Sum

- Link: https://leetcode.com/problems/3sum/
- Difficulty: Medium
- Topics: Array, Sort, Two pointer 

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

Constraints:

* 3 <= nums.length <= 3000
* -10^5 <= nums[i] <= 10^5


UMPIRE Method:

Understand

- Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
- Choose a “happy path” test input, different than the one provided, and a few edge case inputs.
- Verify that you and the interviewer are aligned on the expected inputs and outputs.

1. Can the input array be empty? (No)
2. Any requirement on time complexity?
3. Is the array sorted? (No)
4. Can I modify the array? (Yes)

Match 

- See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category

1. Sort: If first sort the array, we can skip repeated values
2. Pointers: Since duplicate values will be next to each other, it is easier to skip them with pointers

Plan 

- Sketch visualizations and write pseudocode
- Walk through a high level implementation with an existing diagram

1. Sort the input array
2. Initialize the result array
3. Iterate through the array
    - If i > 0 and the value is same as the previous value
        - Skip this value(Since we already find the triples that start with this value)
    - Intialize the two pointers, left and right, where left starts from i + 1 and right starts from the end of the array, i represents the current index of the element n
    - While left pointer is less than the right pointer
        - Add the three nums (current num, left, right)
        - If equal to 0, append the indices, increment the left pointer, while the left pointer is pointing to the same value as the previous and left is less than right, skip the value (Avoid the second value starting from the same value)
        - If greater than 0, right pointer decrement
        - If less than 0, left pointer increment
4. Return result array
    
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
- Time complexity: O(N^2)
- Space complexity: O(N)
