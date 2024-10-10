49. Group Anagrams

- Link: https://leetcode.com/problems/group-anagrams/description/
- Difficulty: Medium
- Topics: Array, Hash map, String, Sorting

Given an array of strings strs, group the 
anagrams
 together. You can return the answer in any order.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation: 
- There is no string in strs that can be rearranged to form "bat".
- The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
- The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

Example 2:

Input: strs = [""]
Output: [[""]]

Example 3:

Input: strs = ["a"]
Output: [["a"]]

Constraints:

* 1 <= strs.length <= 10^4
* 0 <= strs[i].length <= 100
* strs[i] consists of lowercase English letters.


UMPIRE Method:

Understand

- Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
- Choose a “happy path” test input, different than the one provided, and a few edge case inputs.
- Verify that you and the interviewer are aligned on the expected inputs and outputs.

1. Can the input array be empty? 
2. Any requirement on time complexity?

Match 

- See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category

1. Sorting: We can sort each string in the array and compare them. But the time complexity can be high (O(m x nlogn))
2. Hash map: Using a hash map to store the character count of each words use and its corresponding words of the array enables us to efficiently maintain the association (O(m x n))

Plan 

- Sketch visualizations and write pseudocode
- Walk through a high level implementation with an existing diagram

General Idea: Create a hash map to store charCount (array as key) and list of anagrams (array as value)

1. Create a hash map (default dict)
2. Iterate through the strs array
    - For each str, declare a count array with 26 zeroes
        - For each c in str, get the index in the count array and add 1
        - Append the key value pair to the hash map (key is the count array and value is the str) (in python list cannot be key, so we have to turn it into tuples)
3. Return the values of the hash map
    
Implement 

- Implement the solution (make sure to know what level of detail the interviewer wants)

See solution.py

Review

- Re-check that your algorithm solves the problem by running through important examples
- Go through it as if you are debugging it, assuming there is a bug

Evaluate 

- Finish by giving space and run-time complexity
- Discuss any pros and cons of the solution

Assume M represents the number of words in the array, N represents the average length of each word.
- Time complexity: O(M x N)
- Space complexity: O(M)
