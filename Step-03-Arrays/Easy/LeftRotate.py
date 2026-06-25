"""
Problem :
Given an integer array nums, rotate the array to the left by one.
Note: There is no need to return anything, just modify the given array.

Example 1 : Input: nums = [1, 2, 3, 4, 5]
            Output: [2, 3, 4, 5, 1]
            Explanation : Initially, nums = [1, 2, 3, 4, 5]
                          Rotating once to left -> nums = [2, 3, 4, 5, 1]

                          
Approach :
1. Create a temporary array temp of size n.
2. Copy all elements from index 1 to n-1 into temp starting from index 0.
3. Place the first element of the original array at the last index of temp.
4. Print the elements of temp

Time Complexity : O(n)
Space Complexity : O(n)
"""
# Brute Force
class Solution:
    def leftRotate(self,arr,n):
        temp = [0] * n
        
        for i in range(1,n):
             temp[i - 1] = arr[i]
        temp[n - 1] = arr[0]

        for num in temp:
            print(num, end=" ")
        print()
        
if __name__ == "__main__":
    sol = Solution()
    n = 5
    arr = [1,2,3,4,5]
    sol.leftRotate(arr,n)


# Optimal Solution
"""
Approach :
1. Store the first element of the array in a temporary variable.
2. Shift every element one position to the left.
3. Place the stored first element at the last index.
4. Return the modified array.

Time Complexity : O(n)
Space Complexity : O(1)
"""

class Solution:
    def leftRotate(self,arr):
        temp = arr[0]
        n = len(arr)
        for i in range(1,n):
            arr[i-1] = arr[i]
        arr[n-1] = temp
        return arr
        
if __name__ == "__main__":
    sol = Solution()
    arr = [1,2,3,4,5]
    print(sol.leftRotate(arr))