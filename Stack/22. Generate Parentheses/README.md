22. Generate Parentheses

- Link: https://leetcode.com/problems/generate-parentheses/description/
- Difficulty: Medium
- Topics: String, Stack, Backtracking

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:

Input: n = 1
Output: ["()"]


Constraints:

- 1 <= n <= 8

UMPIRE Method:

Understand

- Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
- Choose a “happy path” test input, different than the one provided, and a few edge case inputs.
- Verify that you and the interviewer are aligned on the expected inputs and outputs.

1. When you mention combinations, does that mean we need to generate all possible valid combinations, or are there specific criteria for what constitues a valid combination?
2. Can we assume that the input n will always be a non-negative integer?
3. If n = 2, can you provide an example of the expected output? This will help clarify what is meant by combinations of well-formed parentheses

Match

- See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category

1. Stack: Stack is useful here to help keep track of the current parenthesis sequence being formed
2. Backtracking: Backtracking approach ensures that all valid combinations of parentheses are systematically generated
 
Plan

- Sketch visualizations and write pseudocode
- Walk through a high level implementation with an existing diagram

General Idea: 
1. We can only add close parenthesis when the number of close parenthesis is less than open parenthesis
2. We will at most have n open and n close parentheses in every combination

Steps:
1. Initialization: 
    - Create an empty list res to store valid parenthesis combinations
    - Create an empty stack to keep track of the current parenthesis sequence being formed
2. Define Backtracking function (backtrack):
    - Define a recursive function backtrack that takes counts of open and close parentheses as parameters 
    - Base Case:
        - If counts of open and close parentheses both equal to n, add the current combination in the stack to the result list (res)
        - Return to backtrack and explore other possibilities
    - Recursive Step:
        - Try adding an open parenthesis if the count of open parentheses is less than n
        - Append an open parenthesis to the stack
        - Recursively call backtrack with an incremented count of open parentheses (open + 1)
        - Pop the last character from the stack to backtrack and explore other possibilities
        - Try adding a close parenthesis if the count of close parentheses is less than the count of open parentheses
        - Append a closing parenthesis to the stack
        - Recursively call backtrack with an incremented count of close parentheses 
        - Pop the last character from the stack to backtrack and explore other possibilities
3. Start Backtracking
4. Return Result

Implement

- Implement the solution (make sure to know what level of detail the interviewer wants)

See solution.py

Review

- Re-check that your algorithm solves the problem by running through important examples
- Go through it as if you are debugging it, assuming there is a bug

Evaluate

- Finish by giving space and run-time complexity
- Discuss any pros and cons of the solution

Assume N is the number of pairs.

- Time complexity: O(2^N)
- Space complexity: O(N)
