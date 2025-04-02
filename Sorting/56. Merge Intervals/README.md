56. Merge Intervals

- Link: https://leetcode.com/problems/merge-intervals/description/
- Difficulty: Medium
- Topics: Array, Sorting

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Constraints:

- 1 <= intervals.length <= 10^4
- intervals[i].length == 2
- 0 <= starti <= endi <= 10^4

UMPIRE Method:

Understand

- Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
- Choose a “happy path” test input, different than the one provided, and a few edge case inputs.
- Verify that you and the interviewer are aligned on the expected inputs and outputs.

1. Can the input be empty? (No)
2. Any requirement on time/space complexity? (O(NlogN) in time and O(N) in space)
3. Are [1, 4] and [4, 5] considered overlapping? (Yes)
4. Can we assumed the intervals array sorted? (No)

Match

- See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category

1. Sorting
   First sort the array based on the start time, so that we can check whether the intervals are overlapping in one pass. If we don't sort the array, we will have to have a nested loop to check that, which takes O(N^2) time. Sorting takes only O(NLogN) time.

Plan

- Sketch visualizations and write pseudocode
- Walk through a high level implementation with an existing diagram

1. First Sort the intervals array based on start time.
2. Declare an output array, initialize it with the first interval in it.
3. Iterate through the intervals to check whether it overlapps with the previous interval in the output array (the start time is less than or equal to the previous end time).
   - If overlapping, change the previous end time to max of current end and previous end to present the merge.
   - If not overlapping, append the interval to the output.
4. Return the output array.

Implement

- Implement the solution (make sure to know what level of detail the interviewer wants)

See solution.py

Review

- Re-check that your algorithm solves the problem by running through important examples
- Go through it as if you are debugging it, assuming there is a bug

Evaluate

- Finish by giving space and run-time complexity
- Discuss any pros and cons of the solution

Assume N intervals in intervals array

- Time Complexity: O(NLogN)
- Space Complexity: O(N)
