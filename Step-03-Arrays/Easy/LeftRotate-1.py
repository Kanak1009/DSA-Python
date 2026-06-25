"""
Problem :
Given an integer array nums and a non-negative integer k, rotate the array to the left by k steps.

Example 1 : Input: nums = [1, 2, 3, 4, 5, 6], k = 2
            Output: nums = [3, 4, 5, 6, 1, 2]
            Explanation :   rotate 1 step to the left: [2, 3, 4, 5, 6, 1]
                            rotate 2 steps to the left: [3, 4, 5, 6, 1, 2]

                          
Approach :
1. Compute the effective number of rotations:
    d = d % n
This handles cases where d > n.

2. Store the first d elements in a temporary array.
3. Shift the remaining n - d elements to the left by d positions.
4. Copy the stored elements from the temporary array to the end of the array.
5. Return the rotated array.

Time Complexity : O(n)
Space Complexity : O(d)
"""
# Brute Force
class Solution:
    def leftRotate(self,arr,n,d):
        d = d % n
        temp = []
        for i in range(0,d):
            temp.append(arr[i])
        for i in range(d,n):
            arr[i-d] = arr[i]
        for i in range(n-d,n):
            arr[i] = temp[i-(n-d)]
        return arr
if __name__ == "__main__":
    sol = Solution()
    arr = [1,2,3,4,5,6,7]
    n = len(arr)
    d = 3
    print(sol.leftRotate(arr,n,d))


# Optimal Solution
"""
Approach :
1. Compute the effective number of rotations:
        d = d % n
2. Reverse the first d elements.
3. Reverse the remaining n - d elements.
4. Reverse the entire array.
5. The array is now left-rotated by d positions.

Time Complexity : O(n)
Space Complexity : O(1)
"""

class Solution:
    def reverse(self, arr, start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
    # For rightRotate:
    # def rightRotate(self, arr, n, d):
    #     if n == 0:
    #         return arr
    #     d = d % n
    #     self.reverse(arr, 0, n - 1)
    #     self.reverse(arr, 0, d - 1)
    #     self.reverse(arr, d, n - 1)
    #     return arr

    def leftRotate(self, arr, n, d):
        if n == 0:
            return arr
        d = d % n
        self.reverse(arr, 0, d - 1)
        self.reverse(arr, d, n - 1)
        self.reverse(arr, 0, n - 1)
        return arr

if __name__ == "__main__":
    sol = Solution()
    arr = [1, 2, 3, 4, 5, 6, 7]
    n = len(arr)
    d = 3

    print(sol.leftRotate(arr, n, d))