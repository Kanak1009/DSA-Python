"""
Problem :
Given an array of integers nums, sort the array in non-decreasing order using the recursive Bubble Sort algorithm, 
and return the sorted array.
You must implement Bubble Sort using recursion only.
Do not use built-in sorting functions (sort, sorted, Arrays.sort, etc.).
A sorted array in non-decreasing order is an array where each element is greater than or equal to the previous one.

Example 1 : Input: nums = [7, 4, 1, 5, 3]
            Output: [1, 3, 4, 5, 7]
            Explanation: 1 <= 3 <= 4 <= 5 <= 7.
Thus the array is sorted in non-decreasing order.


Approach :
This is the recursive version of Bubble Sort.
1. In one pass, compare adjacent elements and swap them if they are in the wrong order.
2. After the pass, the largest element among the first n+1 elements moves to its correct position at index n.
3. Recursively call Bubble Sort for the remaining unsorted portion (0 to n-1).
4. Stop when n == 0.

Time Complexity : 
Best Case: O(n²)
Average Case: O(n²)
Worst Case: O(n²)
Space Complexity : O(n)
"""
# Brute Force
class Solution:
    def bubbleSort(self, nums, n):
        if n == 0:
            return
        for j in range(0, n):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

        self.bubbleSort(nums, n - 1)


if __name__ == "__main__":
    sol = Solution()
    nums = [13, 46, 24, 52, 20, 9]

    sol.bubbleSort(nums, len(nums) - 1)
    print(*nums)


# Optimal Approach
"""
Approach :
This is the optimized recursive Bubble Sort.

1. Perform one Bubble Sort pass on the first n elements.
2. During the pass:
    Compare adjacent elements.
    Swap them if they are in the wrong order.
    Set didSwap = 1 whenever a swap occurs.
3. If no swaps occur (didSwap == 0), the array is already sorted, so stop recursion.
4. Otherwise, recursively sort the first n - 1 elements.
5. Base case:
    If n == 1, return

Time Complexity : 
Best Case: O(n)
Average Case: O(n²)
Worst Case: O(n²)
Space Complexity : O(n)
"""
class Solution:
    def bubbleSort(self, nums, n):
        if n == 1:
            return
        didSwap = 0
        for j in range(0, n - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                didSwap = 1
        if didSwap == 0:
            return
        self.bubbleSort(nums, n - 1)


if __name__ == "__main__":
    sol = Solution()
    nums = [13, 46, 24, 52, 20, 9]

    sol.bubbleSort(nums, len(nums))
    print(*nums)