215. Kth Largest Element in an Array

- Link: https://leetcode.com/problems/kth-largest-element-in-an-array/description/
- Difficulty: Medium
- Topics: Array, Heap, Divide and Conquer, QuickSelect

Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4

Constraints:

* 1 <= k <= nums.length <= 10^5
* -10^4 <= nums[i] <= 10^4


UMPIRE Method:

Understand

- Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
- Choose a “happy path” test input, different than the one provided, and a few edge case inputs.
- Verify that you and the interviewer are aligned on the expected inputs and outputs.

1. Will k be smaller or equal to the array length? (Yes)
2. Any requirement on time complexity? (A solution in O(n* logn) time complexity is ok but can you do better?)
3. Should we assume the nums array unsorted? (Yes)

Match 

- See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category

1. Heap: The core task of finding the kth largest or kth smallest element in a collection is a classic example of an order statistics problem. Heaps are useful because they can efficiently maintain order properties. We don't need the whole array sorted. If we are only interested in a subset of the sorted elements (like the kth largest), a heap efficiently provides access to these elements without the overhead of fully sorting the data.

Plan 

- Sketch visualizations and write pseudocode
- Walk through a high level implementation with an existing diagram

General Idea: The min heap generally keeps track of the k largest elements seen so far. By maintaining size k, we ensure that the smaller elements are discarded, and only the k largest elements remain. When we finish building the size k min heap, the smallest value in the heap would be the kth largest element in the entire array.

1. Initialize a min heap
    - Create an empty array called minHeap
2. Iterate through the nums array
    - Loop through each num in nums
3. Build and Maintain the heap
    - Add num to minHeap by using heapq.heappush()
    - Check if the size exceeds k. If yes, remove the smallest element by using heapq.heappop()
4. Return the kth largest value
    - Return minHeap[0]
    
Implement 

- Implement the solution (make sure to know what level of detail the interviewer wants)

See solution.py

Review

- Re-check that your algorithm solves the problem by running through important examples
- Go through it as if you are debugging it, assuming there is a bug

Evaluate 

- Finish by giving space and run-time complexity
- Discuss any pros and cons of the solution

Assume N represents the number of items in the array
- Time complexity: O(NlogK)
- Space complexity: O(N)
