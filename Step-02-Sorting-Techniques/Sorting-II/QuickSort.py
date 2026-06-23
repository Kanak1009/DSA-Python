"""
Problem :
Given an array of integers called nums, sort the array in non-decreasing order using the quick sort algorithm 
and return the sorted array.A sorted array in non-decreasing order is an array where each element is greater than or 
equal to all preceding elements in the array.

Example 1 : Input: nums = [7, 4, 1, 5, 3]
            Output: [1, 3, 4, 5, 7]
            Explanation: 1 <= 3 <= 4 <= 5 <= 7.
Thus the array is sorted in non-decreasing order.


Approach :
Quick Sort is a Divide and Conquer algorithm.

1.Choose a pivot element.
    In the code, the first element is chosen as the pivot:
        pivot = arr[low]
2.Partition the array:
    Place all elements smaller than or equal to the pivot on the left.
    Place all elements greater than the pivot on the right.
    Put the pivot in its correct sorted position.
3. Recursively apply Quick Sort on:
    Left subarray
    Right subarray
4. Continue until the subarray contains 0 or 1 element.

Time Complexity : 
Best Case: O(n log n)
Average Case: O(n log n)
Worst Case: O(n²)
Space Complexity : 
Best/Average: O(log n)
Worst: O(n)
"""

class Solution:
    def partition(self, arr, low, high):
        pivot = arr[low]
        i = low
        j = high

        while i < j:
            while i <= high - 1 and arr[i] <= pivot:
                i += 1

            while j >= low + 1 and arr[j] > pivot:
                j -= 1

            if i < j:
                arr[i], arr[j] = arr[j], arr[i]

        arr[low], arr[j] = arr[j], arr[low]
        return j

    def quicksort(self, arr, low, high):
        if low < high:
            pIndex = self.partition(arr, low, high)
            self.quicksort(arr, low, pIndex - 1)
            self.quicksort(arr, pIndex + 1, high)

    def quickSort(self, arr):
        self.quicksort(arr, 0, len(arr) - 1)


if __name__ == "__main__":
    sol = Solution()
    arr = [13, 46, 24, 20, 52, 9]
    sol.quickSort(arr)
    print(*arr)