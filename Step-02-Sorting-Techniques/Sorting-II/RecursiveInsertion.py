"""
Problem :
Given an array of integers nums, sort the array in non-decreasing order using the recursive Insertion Sort algorithm, 
and return the sorted array.
You must implement Insertion Sort using recursion only.
Do not use loops (like for or while) or built-in sorting functions (sort, Arrays.sort, etc.).
A sorted array in non-decreasing order is an array where each element is greater than or equal to all elements that come before it.

Example 1 : Input: nums = [7, 4, 1, 5, 3]
            Output: [1, 3, 4, 5, 7]
            Explanation: 1 <= 3 <= 4 <= 5 <= 7.
Thus the array is sorted in non-decreasing order.


Approach :
1. Assume the first element is already sorted.
2. Pick the next element (key) from the unsorted portion.
3. Compare key with elements in the sorted portion from right to left.
4. Shift all elements greater than key one position to the right.
5. Insert key into its correct position.
6. Repeat until the entire array becomes sorted.

Time Complexity : 
Best Case: O(n)
Average Case: O(n²)
Worst Case: O(n²)
Space Complexity : O(1)
"""

class Solution:
    def insertionSort(self, nums, i, n):
        if i == n:
            return
        key = nums[i]
        j = i - 1

        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key
        self.insertionSort(nums, i + 1, n)


if __name__ == "__main__":
    sol = Solution()
    nums = [13, 46, 24, 52, 20, 9]

    sol.insertionSort(nums, 1, len(nums))
    print(nums)
