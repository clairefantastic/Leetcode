125. Valid Palindrome

- Link: https://leetcode.com/problems/valid-palindrome/description/
- Difficulty: Easy
- Topics: String, Two pointers

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.


Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.


Constraints:

* 1 <= s.length <= 2 * 10^5
* s consists only of printable ASCII characters


UMPIRE Method:

Understand

- Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
- Choose a “happy path” test input, different than the one provided, and a few edge case inputs.
- Verify that you and the interviewer are aligned on the expected inputs and outputs.

1. Are there any specific edge cases you'd like the solution to handle? For example, empty strings, strings with only one character, or strings with only non-alphanumeric characters? (You should handle all of them)
2. Any requirement on time complexity? (O(n) time and O(1) space will do.)

Match 

- See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category

1. Two pointers: Since we got a hint that this question should be solved in O(1) space complexity, instead of using string manipulation or array to brute force the problem, we can simply use two pointers to neglect characters that are not valid. This approach allows us to evaluate the palindrome property in place, without the need for additional data structures.

Plan 

- Sketch visualizations and write pseudocode
- Walk through a high level implementation with an existing diagram

General Idea: With two pointers, one at the beginning and one at the end of the string, we can compare the characters these pointers refer to. If both characters are alphanumeric and identical (considering case insensitivity), we move the pointers closer to the center of the string, continuing this process. Whenever we encounter non-alphanumeric characters, we can skip them by moving the respective pointer inwards. This way, we efficiently ignore invalid characters and focus only on the parts of the string that matter for palindrome validation.

1. Initialize Pointers
- Start with two pointers, left at the beginning and right at the end of the string.
2. Turn the string to lowercase
3. Traverse String with Pointers
- Use a while loop to move left and right towards each other, stopping when they meet or cross.
4. Skip Non-Alphanumeric Characters
- Inside the loop, increment left and decrement right to skip over any non-alphanumeric characters, remember checking whether l is less than right again 
5. Character Comparison
- Compare the characters at left and right indices. If they match, move left one step right and right one step left, then repeat the comparison.
- If characters not matching, return False.
6. Complete Check
- If the loop completes without mismatches, return True, indicating the string is a palindrome.

    
Implement 

- Implement the solution (make sure to know what level of detail the interviewer wants)

See solution.py

Review

- Re-check that your algorithm solves the problem by running through important examples
- Go through it as if you are debugging it, assuming there is a bug

Evaluate 

- Finish by giving space and run-time complexity
- Discuss any pros and cons of the solution

Assume N represents the length of the string.
- Time complexity: O(N)
- Space complexity: O(1)

