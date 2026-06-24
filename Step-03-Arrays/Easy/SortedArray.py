"""
Problem :
Given an array nums of n integers, return true if the array nums is sorted in non-decreasing order or else false.
Example 1 : Input : nums = [1, 2, 3, 4, 5]
            Output : true
            Explanation : For all i (1 <= i <= 4) it holds nums[i] <= nums[i+1], hence it is sorted and we return true.


Approach :
1. Traverse the array from index 1 to n-1.
2. Compare each element with its previous element:
    If arr[i] >= arr[i-1], continue.
3. Otherwise, the array is not sorted, so return False.
4. If the loop completes without finding any violation, return True

Time Complexity : 
Best Case: O(1)
Average Case: O(n)
Worst Case: O(n)
Space Complexity : O(1)
"""
# Brute Force
class Solution:
    def sortedArray(self,arr,n):
        for i in range(1,n):
            if arr[i] >= arr[i-1]:
                pass
            else:
                return False
        return True
        
if __name__ == "__main__":
    sol = Solution()
    arr = [24,1,4,12,5]
    # arr = [1,4,5,12,24]
    n = len(arr)
    print(sol.sortedArray(arr,n))

# Optimal Solution
"""
Approach :
1. Traverse the array from index 1 to n-1.
2. Compare each element with its previous element.
3. If at any point:
    arr[i] < arr[i - 1]
    the array is not sorted, so return False.
4. If no such pair is found, return True.

Time Complexity : O(n)
Space Complexity : O(1)
"""
class Solution:
    def sortedArray(self,arr,n):
        for i in range(1,n):
            if arr[i] < arr[i-1]:
                return False
        return True
        
if __name__ == "__main__":
    sol = Solution()
    # arr = [24,1,4,12,5]
    arr = [1,4,5,12,24]
    n = len(arr)
    print(sol.sortedArray(arr,n))