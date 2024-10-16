347. Top K Frequent Elements

- Link: https://leetcode.com/problems/top-k-frequent-elements/description/
- Difficulty: Medium
- Topics: Array, Sorting, Hashing, Heap

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:

Input: nums = [1], k = 1
Output: [1]

Constraints:

* 1 <= nums.length <= 10^5
* -10^4 <= nums[i] <= 10^4
* k is in the range [1, the number of unique elements in the array].
* It is guaranteed that the answer is unique.


UMPIRE Method:

Understand

- Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
- Choose a “happy path” test input, different than the one provided, and a few edge case inputs.
- Verify that you and the interviewer are aligned on the expected inputs and outputs.

1. Can the nums array be empty?
2. Any requirement on time complexity?
3. Is the array sorted?
4. Will different numbers have the same frequency. If yes, what should I return in this situation?

Match 

- See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category

1. Hash Map with Frequency Count and Sorting:   
    Create a hash map to count the frequency of each element in the array. Sort the elements based on their frequencies.
    Return the top k elements from the sorted list. This method will have the total time complexity of O(nlogn) due to the sorting step.
    Can we do better?
2. Priority Queue (Heap):
    Create a max-heap to maintain the k most frequent elements. Iterate through the array, updating the heap as you encounter elements. The heap will always contain the k most frequent elements, and this method has a time complexity of O(klogn).
    Can we do better?
3. Bucket Sort:
    Since k is bounded by the array size (k is never gonna exceed the array size n). We can use a hash mpa to count the frequency of each element. Create an array of "buckets", where each bucket corresponds to a specific frequency count (index = frequency) Place elements into their respective buckets based there freqencies. Start from the highest-frequency bucket and collect elements until you have k elements. This method can be efficient since the time/space complexity are both O(n)

Plan 

- Sketch visualizations and write pseudocode
- Walk through a high level implementation with an existing diagram

General Idea: Create a hash map to count the frequency of each element. Place elements into their respective buckets based on their frequencies. The numbers of buckets will be the length of the array at most.

1. Create a hash map for count
    - Count the frequency of each number
2. Create a frequency array for each numeber in the list
    - Use the frequency as an index and append the number to the corresponding frequency bucket (bucket sort)
3. Append the numbers to the list in descending order of their frequency
    - Continue appending until the length of the list is equal to k
4. Return the top k elements from the list
    
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
- Space complexity: O(N)
