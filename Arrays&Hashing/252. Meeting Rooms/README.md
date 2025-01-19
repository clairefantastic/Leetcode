252. Meeting Rooms

- Link: https://leetcode.com/problems/meeting-rooms/description/
- Difficulty: Easy
- Topics: Array, Sorting

Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend all meetings.

Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: false

Example 2:

Input: intervals = [[7,10],[2,4]]
Output: true

Constraints:

* 0 <= intervals.length <= 104
* intervals[i].length == 2
* 0 <= starti < endi <= 106


UMPIRE Method:

Understand

- Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
- Choose a “happy path” test input, different than the one provided, and a few edge case inputs.
- Verify that you and the interviewer are aligned on the expected inputs and outputs.

1. Can the interval array be empty?
2. Any requirement on time complexity?
3. Is the array sorted?
4. Will the numbers in the array duplicate?
5. What is the data structure of each interval? Is it array or tuple?
6. Will the start time ever exceed the end time or will the they be the same in each interval?
7. If the two intevals, one start time is equal to the other's end time, can they be defined as conflict?

Match 

- See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category

1. Brute Force: Compare every two interval to see if they overlap with each other. However, it will not be efficient because the time complexity will be O(N^2)
2. Sorting: Sort the array based on the start time. The time complexity may be O(NlogN). Since we sort the array based on the start time, when we look at the first two array for example, the second array will never going to start before the first array. From the definition of detecting overlapping, if the second starts after the first array ends, they are not overlapping and we can go to the next two arrays. In this method, we only have to go through the array once.

Plan 

- Sketch visualizations and write pseudocode
- Walk through a high level implementation with an existing diagram

1. Sort the intervals based on their start time
2. Iterate through the interval array (start at the second interval)
    - For each interval, if the previous interval ends after it starts, return False
3. Return True
    
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

