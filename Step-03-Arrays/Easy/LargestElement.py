"""
Problem :
Given an array of integers nums, return the value of the largest element in the array
Example 1 : Input: nums = [3, 3, 6, 1]
            Output: 6
            Explanation: The largest element in array is 6


Approach :
1. Sort the array in ascending order using:
    nums.sort()
2. After sorting, the largest element will be at the last index.
3. Print the last element:
    nums[-1]

Time Complexity : O(n log n)
Space Complexity : O(n)
"""
# Brute Force
class Solution:
    def largestElement(self, nums):
        nums.sort()
        print(nums[-1])
        
if __name__ == "__main__":
    sol = Solution()
    nums = [24,1,4,12,5]
    sol.largestElement(nums)


# Optimal Solution
"""
Approach :
1. Assume the first element is the largest:
    largest = arr[0]
2. Traverse the array from index 1 to n-1.
3. For each element:
    If the current element is greater than largest, update largest.
4. After traversing the entire array, largest will contain the maximum element.
5. Print the result.

Time Complexity : O(n)
Space Complexity : O(1)
"""
class Solution:
    def largestElement(self,arr,n):
        largest = arr[0]
        for i in range(1,n):
            if arr[i] > largest:
                largest = arr[i]
        print(largest)
        
if __name__ == "__main__":
    sol = Solution()
    arr = [24,1,4,12,5]
    n = len(arr)
    sol.largestElement(arr,n)