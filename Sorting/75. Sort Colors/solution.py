# Bucket Sort
class Solution(object):
    def sortColors(self, nums):
        count = [0, 0, 0]
        for n in nums:
            count[n] += 1
        nums_i = 0
        for count_i in range(len(count)):
            for i in range(count[count_i]):
                nums[nums_i] = count_i
                nums_i += 1
        return nums
        
# Quick Sort
class Solution(object):
    def sortColors(self, nums):
        l, r = 0, len(nums) - 1
        i = 0

        def swap(i, j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

        while i <= r:
            if nums[i] == 0:
                swap(l, i)
                l += 1
            elif nums[i] == 2:
                swap(i, r)
                r -= 1
                i -= 1
            i += 1
