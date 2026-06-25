"""
Problem :
Given an array of integers nums and an integer target, find the smallest index (0 based indexing) where the 
target appears in the array.If the target is not found in the array, return -1

Example 1 : Input: nums = [2, 3, 4, 5, 3], target = 3
            Output: 1
            Explanation : The first occurence of 3 in nums is at index 1
                          
Approach :
1. Traverse the array from the first element to the last.
2. Compare each element with the target value (num).
3. If a match is found, return its index.
4. If the entire array is traversed without finding the element, return -1.

Time Complexity : 
Best Case: O(1)
Average Case: O(n)
Worst Case: O(n)
Space Complexity : O(1)
"""

class Solution:
    def linearSearch(self, arr, num):
        n = len(arr)
        for i in range(n):
            if arr[i] == num:
                return i
        return -1

if __name__ == "__main__":
    sol = Solution()
    arr = [1, 2, 3, 4, 5]
    num = 4
    print(sol.linearSearch(arr, num))
