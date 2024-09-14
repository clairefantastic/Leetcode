278. First Bad Version

- Link: https://leetcode.com/problems/first-bad-version/description/
- Difficulty: Easy 
- Topics: Binary Search

You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

Example 1:

Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.

Example 2:

Input: n = 1, bad = 1
Output: 1

Constraints:

- 1 <= bad <= n <= 2^31 - 1


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
- While the left pointer is less than the right pointer
    - Calculate the mid
    - If isBadVersion(mid), right will become mid
    - If not, left will become mid + 1
- Return the left pointer
    
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
