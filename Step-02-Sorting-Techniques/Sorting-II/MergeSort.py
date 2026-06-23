"""
Problem :
Given an array of integers, nums,sort the array in non-decreasing order using the merge sort algorithm. Return the sorted array.
A sorted array in non-decreasing order is one in which each element is either greater than or equal to all the elements to its left in the array.
Example 1 : Input: nums = [7, 4, 1, 5, 3]
            Output: [1, 3, 4, 5, 7]
            Explanation: 1 <= 3 <= 4 <= 5 <= 7.
Thus the array is sorted in non-decreasing order.


Approach :
Merge Sort follows the Divide and Conquer technique.
1. Divide the array into two halves.
2. Recursively sort the left half.
3. Recursively sort the right half.
4. Merge the two sorted halves into a single sorted array.

Code has two functions:
    mergeSort() → Divides the array recursively.
    merge() → Combines two sorted halves.

Time Complexity : 
Best Case: O(n log n)
Average Case: O(n log n)
Worst Case: O(n log n)
Space Complexity : O(n)
"""

class Solution:
    def merge(self, arr, low, mid, high):
        temp = []
        left, right = low, mid + 1

        while left <= mid and right <= high:
            if arr[left] <= arr[right]:
                temp.append(arr[left])
                left += 1
            else:
                temp.append(arr[right])
                right += 1

        while left <= mid:
            temp.append(arr[left])
            left += 1

        while right <= high:
            temp.append(arr[right])
            right += 1

        for i in range(low, high + 1):
            arr[i] = temp[i - low]

    def mergeSort(self, arr, low, high):
        if low >= high:
            return
        mid = (low + high) // 2
        self.mergeSort(arr, low, mid)
        self.mergeSort(arr, mid + 1, high)
        self.merge(arr, low, mid, high)


if __name__ == "__main__":
    arr = [13,46,24,52,20,9]
    sol = Solution()
    sol.mergeSort(arr, 0, len(arr) - 1)
    print(*arr)

