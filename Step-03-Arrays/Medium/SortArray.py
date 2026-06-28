"""
Problem :
Given an array nums consisting of only 0, 1, or 2. Sort the array in non-decreasing order.
The sorting must be done in-place, without making a copy of the original array.

Example 1 : Input: nums = [1, 0, 2, 1, 0]
            Output: [0, 0, 1, 1, 2]
            Explanation : The nums array in sorted order has 2 zeroes, 2 ones and 1 two


Approach :
1. Traverse the array once and count the number of: 
    0s
    1s
    2s
2. Traverse the array again:
    Fill the first count0 positions with 0.
    Fill the next count1 positions with 1.
    Fill the remaining positions with 2.
3. The array is sorted in-place.

Time Complexity : O(n)
Space Complexity : O(1)
"""
# Brute Force
class Solution:
    def sortZeroOneTwo(self, nums):
        count0 = count1 = count2 = 0
        for num in nums:
            if num == 0:
                count0 += 1
            elif num == 1:
                count1 += 1
            else:
                count2 += 1
        index = 0
        for _ in range(count0):
            nums[index] = 0
            index += 1
        for _ in range(count1):
            nums[index] = 1
            index += 1
        for _ in range(count2):
            nums[index] = 2
            index += 1

if __name__ == "__main__":
    nums = [1, 0, 2, 1, 0]
    sol = Solution()
    sol.sortZeroOneTwo(nums)
    print(nums)


# Better Approach
"""
Approach :
1. Traverse the array once and count the occurrences of:
    0s (cnt0)
    1s (cnt1)
    2s (cnt2)
2. Overwrite the array:
    Fill the first cnt0 positions with 0.
    Fill the next cnt1 positions with 1.
    Fill the remaining positions with 2.
3. The array becomes sorted in-place.

Time Complexity : O(n)
Space Complexity : O(1)
"""
class Solution:
    def sortZeroOneTwo(self, nums):
        cnt0 = cnt1 = cnt2 = 0
        for num in nums:
            if num == 0:
                cnt0 += 1
            elif num == 1:
                cnt1 += 1
            else:
                cnt2 += 1

        for i in range(cnt0):
            nums[i] = 0

        for i in range(cnt0, cnt0 + cnt1):
            nums[i] = 1

        for i in range(cnt0 + cnt1, len(nums)):
            nums[i] = 2

if __name__ == "__main__":
    nums = [1, 0, 2, 1, 0]
    sol = Solution()
    sol.sortZeroOneTwo(nums)
    print(nums)



# Optimal Solution : Two Pointers
"""
Approach :
Maintain three pointers:
low → Boundary for 0s.
mid → Current element being processed.
high → Boundary for 2s.

During traversal:
If nums[mid] == 0:
    Swap nums[low] and nums[mid].
    Increment both low and mid.
If nums[mid] == 1:
    1 is already in the correct region.
    Increment mid.
If nums[mid] == 2:
    Swap nums[mid] and nums[high].
    Decrement high.
    Do not increment mid, because the swapped element must be checked

Time Complexity : O(n)
Space Complexity : O(1)
"""
class Solution:
   def sortZeroOneTwo(self, nums):
        low, mid, high = 0, 0, len(nums) - 1
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1

if __name__ == "__main__":
    nums = [1, 0, 2, 1, 0]
    sol = Solution()
    sol.sortZeroOneTwo(nums)
    print(nums)
