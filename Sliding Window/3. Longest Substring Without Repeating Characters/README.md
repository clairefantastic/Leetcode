3. Longest Substring Without Repeating Characters

- Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
- Difficulty: Medium 
- Topics: String, Sliding Window

Given a string s, find the length of the longest 
substring
 without repeating characters.


Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:

- 0 <= s.length <= 5 * 10^4
- s consists of English letters, digits, symbols and spaces.


UMPIRE Method:

Understand

- Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
- Choose a “happy path” test input, different than the one provided, and a few edge case inputs.
- Verify that you and the interviewer are aligned on the expected inputs and outputs.

1. Can the input be empty? (No)
2. Any requirement on time/space complexity?  (O(n) time and O(min(M, N)) space will do) 
3. Are the characters case-sensitive? For example, is 'a' different from 'A'?

Match

- See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category

1. Sliding Window: We can maintain a set to keep track of characters in the current window and use two pointers to represent the start and end of the window. Move the end pointer until a repeating character is found, then move the start pointer to eliminate the repeated character. Keep track of the maximum length of the window.

Plan

- Sketch visualizations and write pseudocode
- Walk through a high level implementation with an existing diagram

General Idea: Record the max length found as we proceed through the array and keep checking whether there is repeating character in the string

1. Initialize a set to keep track of unique characters in the current substring and a left pointer to keep track of the start of the sliding window.
2. Initialize max length to 0
3. Iterate through the string, while the right pointer does not exceed the string length, check if the char the right pointer at is in the set, if yes, remove the element the left pointer points to from the set until the char the right pointer at is not in the set.
4. Add the char the right pointer at to the set
5. Check max length 
6. Return max length
    
Implement

- Implement the solution (make sure to know what level of detail the interviewer wants)

See solution.py

Review

- Re-check that your algorithm solves the problem by running through important examples
- Go through it as if you are debugging it, assuming there is a bug

Evaluate

- Finish by giving space and run-time complexity
- Discuss any pros and cons of the solution

Assume N represents the length of the string and M is the size of the character set.

- Time Complexity: O(N)
- Space Complexity: O(min(M, N))
