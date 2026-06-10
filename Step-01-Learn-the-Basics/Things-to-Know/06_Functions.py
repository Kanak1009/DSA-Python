"""
Problem : Given an array arr of n elements. The task is to reverse the given array. 
          The reversal of array should be inplace.

Example 1 : Input: n=5, arr = [1,2,3,4,5]
            Output: [5,4,3,2,1]
            Explanation: The reverse of the array [1,2,3,4,5] is [5,4,3,2,1]

Example 2 : Input: n=6, arr = [1,2,1,1,5,1]
            Output: [1,5,1,1,2,1]
            Explanation: The reverse of the array [1,2,1,1,5,1] is [1,5,1,1,2,1].


Approach:  1. Slicing, 2. Built-in Method, 3. Using Pointers

Time Complexity:  1. Slicing : O(n)
                  2. Built-in : O(n)
                  3. Pointer : O(n)

Space Complexity :  1. Slicing : O(n)
                    2. Built-in : O(1)
                    3. Pointer : O(1)
"""

class Solution:
    def reverse(self, arr: list) -> None:
    #    arr[:] = arr[::-1]          # Method 1 : Slicing
    #    arr.reverse()               # Method 2 : Built-in function
    #   Method 3 using pointers
        left = 0
        right = len(arr) - 1
        
        while left < right:
            arr[left],arr[right] = arr[right],arr[left]
            left += 1
            right -= 1


if __name__ == "__main__":
    sol = Solution()

    array = [1, 2, 3, 4, 5]
    sol.reverse(array)

    print(array)