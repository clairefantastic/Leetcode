128. Longest Consecutive Sequence

- Link: https://leetcode.com/problems/longest-consecutive-sequence/description/
- Difficulty: Medium
- Topics: Array, Hash

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Constraints:

* 0 <= nums.length <= 10^5
* -10^9 <= nums[i] <= 10^9


UMPIRE Method:

Understand

- Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
- Choose a “happy path” test input, different than the one provided, and a few edge case inputs.
- Verify that you and the interviewer are aligned on the expected inputs and outputs.

1. Can the input array be empty? (Yes)
2. Any requirement on time/space complexity? (O(n) in time)
3. What should I return for an empty array? (0)
4. What should I return if there is no subsequence with consecutive elements? (1)
5. What should we return if there are duplicate elements in the sequence? (Duplicates do not add to the count)

Match 

- See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category

1. Sorting
    We can sort the array of numbers and check if the next item is equal to the previous item add 1. Once we find a match, we keep track of the length of consecutive sequence and return the longest. This works but the time complexity will be O(nlogn)
2. Storing the elements of the array in a HashSet
    As we iterate through the array, we can store each number in a HashSet instantly remove duplicates from our list

Plan 

- Sketch visualizations and write pseudocode
- Walk through a high level implementation with an existing diagram

General Idea: Use a hash set to find the longest length

1. Create a hashset (Pass nums to set)
2. Keep track of longestStreak starting at 0 (Initailize longest at 0)
3. Loop through the number set
    - If current number has no previous number, it means it is the starting element of a sequence, then start counting from this number (length = 0)
        - While the set contains current number + length, increment length 
    - After each while loop, check and set longestStreak
4. Return longestStreak
    
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
