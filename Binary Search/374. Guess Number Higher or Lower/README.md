374. Guess Number Higher or Lower

- Link: https://leetcode.com/problems/guess-number-higher-or-lower/description/
- Difficulty: Easy 
- Topics: Binary Search

We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns three possible results:

-1: Your guess is higher than the number I picked (i.e. num > pick).
1: Your guess is lower than the number I picked (i.e. num < pick).
0: your guess is equal to the number I picked (i.e. num == pick).
Return the number that I picked.

Example 1:

Input: n = 10, pick = 6
Output: 6

Example 2:

Input: n = 1, pick = 1
Output: 1

Example 3:

Input: n = 2, pick = 1
Output: 1

Constraints:

- 1 <= n <= 2^31 - 1
- 1 <= pick <= n

UMPIRE Method:

Understand

- Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
- Choose a “happy path” test input, different than the one provided, and a few edge case inputs.
- Verify that you and the interviewer are aligned on the expected inputs and outputs.

1. Can the input be empty?
2. Any requirement on time/space complexity? (O(logn) in time)

Match

- See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category

1. Binary Search
    - Binary search is a method for locating an element in a sorted list efficiently. Searching for an element can be done naively in O(N) time, but binary search speeds it up to O(logN) time.

Plan

- Sketch visualizations and write pseudocode
- Walk through a high level implementation with an existing diagram

General idea: 
- Set the left, right pointers to 1, n
- While the left pointer is less than or equal to the right pointer
    - Calculate the mid
    - If guess(mid) > 0, left will become mid + 1
    - If guess(mid) < 0, right will become mid - 1
    - Else, return mid
    
Implement

- Implement the solution (make sure to know what level of detail the interviewer wants)

See solution.py

Review

- Re-check that your algorithm solves the problem by running through important examples
- Go through it as if you are debugging it, assuming there is a bug

Evaluate

- Finish by giving space and run-time complexity
- Discuss any pros and cons of the solution

Assume N elements in nums array
- Time Complexity: O(logN)
- Space Complexity: O(1)
