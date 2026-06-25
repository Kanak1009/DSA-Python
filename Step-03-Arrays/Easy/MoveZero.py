"""
Problem :
Given an integer array nums, move all the 0's to the end of the array. 
The relative order of the other elements must remain the same.
This must be done in place, without making a copy of the array.

Example 1 : Input: nums = [0, 1, 4, 0, 5, 2]
            Output: [1, 4, 5, 2, 0, 0]
Explanation : Both the zeroes are moved to the end and the order of the other elements stay the same
                          
Approach :
1. Create a temporary array temp.
2. Traverse the original array and store all non-zero elements in temp.
3. Copy all elements from temp back to the beginning of the original array.
4. Fill the remaining positions with 0.
5. Return the modified array.

Time Complexity : O(n)
Space Complexity : O(n)
"""
# Brute Force
class Solution:
    def moveZeroes(self,arr):
        n = len(arr)
        temp = []
        for i in range(0,n):
            if arr[i] != 0:
                temp.append(arr[i])
        nonZero = len(temp)
        for i in range(0,nonZero):
            arr[i] = temp[i]
        for i in range(nonZero,n):
            arr[i] = 0
        return arr
if __name__ == "__main__":
    sol = Solution()
    arr = [1,0,2,3,2,0,0,4,5,1]
    print(sol.moveZeroes(arr))


# Optimal Solution
"""
Approach :
1. Find the index of the first zero in the array and store it in j.
2. If no zero is found (j == -1), the array is already in the desired form, so return it.
3. Traverse the array from j + 1 to the end:
    Whenever a non-zero element is found, swap it with the element at index j.
    Increment j so that it always points to the next zero position.
4. After the traversal, all non-zero elements are shifted to the front and all zeroes naturally move to the end.

Time Complexity : O(n)
Space Complexity : O(1)
"""

class Solution:
    def moveZeroes(self,arr):
        j = -1
        n = len(arr)
        for i in range(0,n):
            if arr[i] == 0:
                j = i
                break
        if j == -1:
            return arr
        for i in range(j+1,n):
            if arr[i] != 0:
                arr[i],arr[j] = arr[j],arr[i]
                j += 1
        return arr
if __name__ == "__main__":
    sol = Solution()
    arr = [1,0,2,3,2,0,0,4,5,1]
    print(sol.moveZeroes(arr))