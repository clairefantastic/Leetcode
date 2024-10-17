33. Search in a Rotated Sorted Array

- Link: https://leetcode.com/problems/search-in-rotated-sorted-array/description/
- Difficulty: Medium 
- Topics: Binary Search

There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.


Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Example 3:

Input: nums = [1], target = 0
Output: -1

Constraints:

- 1 <= nums.length <= 5000
- -10^4 <= nums[i] <= 10^4
- All values of nums are unique.
- nums is an ascending array that is possibly rotated.
- -10^4 <= target <= 10^4


UMPIRE Method:

Understand

- Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
- Choose a “happy path” test input, different than the one provided, and a few edge case inputs.
- Verify that you and the interviewer are aligned on the expected inputs and outputs.

1. Can the input be empty? (We don't need to consider empty input arrays)
2. Will there be negative numbers? (Possible)
3. Any requirement on time/space complexity? (O(logn) in time)

Match

- See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category

1. Binary Search
    - Binary search is a method for locating an element in a sorted list efficiently. Searching for an element can be done naively in O(N) time, but binary search speeds it up to O(logN) time. Since the given array is sorted, we can apply binary search. However, the array is rotated. So simply apply binary search will not work here.
    
2. Two pointers
    - The two-pointer technique is inherent in binary search, where you typically have left and right pointers. In problems we you need to narrow down a range (like finding a target in a sorted array), using two pointers to adjust the search space is a natural approach.

Plan

- Sketch visualizations and write pseudocode
- Walk through a high level implementation with an existing diagram

General Idea: The goal is to find the inflection point, where the order of elements changes. All elements to the left is greater than the first element, and all elements to the right is less than the first element.

1. Declare left and right pointer (left to 0 and right to the end of the array)
    - While left <= right
        - If nums[mid] == target, return the mid index
        - If nums[l] <= nums[mid], it means that mid is in the left half
            - If target is greater than nums[mid] or less than nums[l], update the left pointer to mid + 1
            - Otherwise, update the right pointer to mid - 1
        - If nums[l] > nums[mid], it means that mid is in the right half
            - If target is less than nums[mid] or greater than nums[r], update the right pointer to mid - 1
            - Otherwise, update the left pointer to mid + 1
2. Return -1 
    
Implement

- Implement the solution (make sure to know what level of detail the interviewer wants)

See solution.py

Review

- Re-check that your algorithm solves the problem by running through important examples
- Go through it as if you are debugging it, assuming there is a bug

Evaluate

- Finish by giving space and run-time complexity
- Discuss any pros and cons of the solution

Assume N numbers in the array.

- Time Complexity: O(logN)
- Space Complexity: O(1)
