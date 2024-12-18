567. Permutation in String 

- Link: https://leetcode.com/problems/permutation-in-string/description/
- Difficulty: Medium 
- Topics: String, Sliding Window

Given two strings s1 and s2, return true if s2 contains a 
permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.


Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false


Constraints:

- 1 <= s1.length, s2.length <= 10^4
- s1 and s2 consist of lowercase English letters.


UMPIRE Method:

Understand

- Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
- Choose a “happy path” test input, different than the one provided, and a few edge case inputs.
- Verify that you and the interviewer are aligned on the expected inputs and outputs.

1. Can the input be empty? (No)
2. Any requirement on time/space complexity?  (O(n) time and O(m) space will do) 
3. Are the characters case-sensitive? For example, is 'a' different from 'A'? (Only lowercase characters)
4. Is it possible s1 is longer than s2? (Yes)

Match

- See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category

1. Sliding Window: Using a sliding window to check if any permutation of s1 is present in s2 by maintaining a moving window and updating character frequencies as the window slides through the input string
2. HashMap: Using a HashMap to keep track of the frequency of characters in the current window

Plan

- Sketch visualizations and write pseudocode
- Walk through a high level implementation with an existing diagram

General Idea: Using a sliding window of the same length as s1 to determine whether the number of occurrences of characters in s2 within this window is equal to the number of occurrences of characters in s1

1. Check the length of s1 and the length of s2 first
    - If the length of s2 is less than the length of s1, return False
2. Character Frequency HashMap Initialization: 
    - Iterate through each character in string s1
    - Populate the char_count_s1 dictionary with the initial frequency of characters in s1
    - Populate the char_count_s2 dictionary with the counts of characters in the initial window of s2 
3. Sliding Window Iteration:
    - Iterate through each character in string s2 using a loop
    - For each character in s2:
        - Update the frequency of the current character in the sliding window
        - Check if the current window's character counts match those of s1
        - Check if the frequency of the character going out of the window has reached zero, if so, remove from the hashmap
        - If the window size is reached, update the frequency for the character going out of the window and continue to slide the window to the right
4. Return Result:
    - Check if the matched count is equal to the length of string s1
    - If true, return True as a permutation of s1 is presented in the current window
    - Else return False
    
Implement

- Implement the solution (make sure to know what level of detail the interviewer wants)

See solution.py

Review

- Re-check that your algorithm solves the problem by running through important examples
- Go through it as if you are debugging it, assuming there is a bug

Evaluate

- Finish by giving space and run-time complexity
- Discuss any pros and cons of the solution

Assume N represents the length of s2 and M is the length of s1.

- Time Complexity: O(N)
- Space Complexity: O(M)
