"""
Problem :
Given an array of integers nums, sort the array in non-decreasing order using the selection sort algorithm and 
return the sorted array.
A sorted array in non-decreasing order is an array where each element is greater than or equal to all previous elements in the array.
Example 1 : Input: nums = [7, 4, 1, 5, 3]
            Output: [1, 3, 4, 5, 7]
            Explanation: 1 <= 3 <= 4 <= 5 <= 7.
Thus the array is sorted in non-decreasing order.


Approach :
1. Divide the array into:
    Sorted part (initially empty)
    Unsorted part (initially the entire array)
2. For each position i:
    Find the index of the smallest element in the unsorted portion.
    Swap it with the element at index i.
3. After each iteration, one more element is placed in its correct sorted position.
4. Repeat until the array is completely sorted.

Time Complexity : 
Best Case, Worst Case and Average Case = O(n²)
Space Complexity : O(1)
"""

class Solution:
    def selectionSort(self, nums):
        n = len(nums)
        for i in range(n-1):
            min_index = i
            for j in range(i+1,n):
                if nums[j] < nums[min_index]:
                    min_index = j
            nums[i],nums[min_index] = nums[min_index],nums[i]
        print(*nums)
if __name__ == "__main__":
    sol = Solution()
    nums = [13,46,24,52,20,9]
    sol.selectionSort(nums)