875. Koko Eating Bananas

- Link: https://leetcode.com/problems/koko-eating-bananas/description/
- Difficulty: Medium 
- Topics: Binary Search

Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

Example 1:

Input: piles = [3,6,7,11], h = 8
Output: 4

Example 2:

Input: piles = [30,11,23,4,20], h = 5
Output: 30

Example 3:

Input: piles = [30,11,23,4,20], h = 6
Output: 23

Constraints:

- 1 <= piles.length <= 10^4
- piles.length <= h <= 10^9
- 1 <= piles[i] <= 10^9


UMPIRE Method:

Understand

- Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
- Choose a “happy path” test input, different than the one provided, and a few edge case inputs.
- Verify that you and the interviewer are aligned on the expected inputs and outputs.

1. Can the input be empty? (We don't need to consider empty inputs)
2. Any requirement on time/space complexity? (O(nlogm) in time and O(1) in space)
3. In this problem, len(p) <= h? (Yes)

Match

- See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category

1. Binary Search
    - Binary search is a method for locating an element in a sorted list efficiently. Searching for an element can be done naively in O(N) time, but binary search speeds it up to O(logN) time.

Plan

- Sketch visualizations and write pseudocode
- Walk through a high level implementation with an existing diagram

- Worst case: When k equals to the maximum number in the piles, koko can finish all the bananas in len(p) hours
    - So we have to loop through the piles array and k from 1 to max(p) (Time complexity may be O(n x m)) 
    - We can then apply binary search to the process to find k from 1 to max(p), the time complexity would be O(nlogm)

- General Idea:
    - Set the left pointer to 1, the right pointer to max(p), and the ans to right 
    - While left is less than or equal to right:
        - Caculate the k (mid) and iterate through the piles array to calculate the hours Koko would have to take to finish all the bananas
        - If the hour is less than or equal to h, ans = k, shift the right pointer to k - 1, 
        - If the hour is greater than h, shift the left pointer to k + 1
    - Return ans 
    
Implement

- Implement the solution (make sure to know what level of detail the interviewer wants)

See solution.py

Review

- Re-check that your algorithm solves the problem by running through important examples
- Go through it as if you are debugging it, assuming there is a bug

Evaluate

- Finish by giving space and run-time complexity
- Discuss any pros and cons of the solution

- Time Complexity: O(nlogm)
- Space Complexity: O(1)
