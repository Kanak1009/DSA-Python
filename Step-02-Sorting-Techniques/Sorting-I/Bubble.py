"""
Problem :
Given an array of integers called nums,sort the array in non-decreasing order using the bubble sort algorithm and return the sorted array.
A sorted array in non-decreasing order is an array where each element is greater than or equal to all preceding elements in the array.
Example 1 : Input: nums = [7, 4, 1, 5, 3]
            Output: [1, 3, 4, 5, 7]
            Explanation: 1 <= 3 <= 4 <= 5 <= 7.
Thus the array is sorted in non-decreasing order.


Approach :
1. Traverse the array multiple times.
2. In each pass, compare adjacent elements:
    If nums[j] > nums[j+1], swap them.
3. After the first pass, the largest element reaches its correct position at the end.
4. After the second pass, the second-largest element reaches its correct position.
5. Continue until the array is completely sorted.

Time Complexity : 
Best Case = O(n)
Average Case and Worst Case = O(n²)
Space Complexity : O(1)
"""
# Brute Force
class Solution:
    def bubbleSort(self, nums):
        n = len(nums)
        for i in range(n-1,0,-1):
            for j in range(0,i):
                if nums[j] > nums[j+1]:
                    nums[j],nums[j+1] = nums[j+1],nums[j]
        print(*nums)
if __name__ == "__main__":
    sol = Solution()
    nums = [13,46,24,52,20,9]
    sol.bubbleSort(nums)


# Optimal Approach
"""
Approach :
1. Compare adjacent elements in the array.
2. If the left element is greater than the right element, swap them.
3. After one complete pass, the largest element "bubbles up" to its correct position at the end.
4. Repeat the process for the remaining unsorted portion.
5. Use a didSwap flag:
    If no swaps occur during a pass, the array is already sorted.
    Stop early using break.

Time Complexity : 
Best Case = O(n)
Average Case and Worst Case = O(n²)
Space Complexity : O(1)

"""
class Solution:
    def bubbleSort(self, nums):
        n = len(nums)
        for i in range(n-1,0,-1):
            didSwap = 0
            for j in range(0,i):
                if nums[j] > nums[j+1]:
                    nums[j],nums[j+1] = nums[j+1],nums[j]
                    didSwap = 1
            if didSwap == 0:
                break
        print(*nums)
if __name__ == "__main__":
    sol = Solution()
    nums = [13,46,24,52,20,9]
    sol.bubbleSort(nums)