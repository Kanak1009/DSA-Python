"""
Problem :
Given an integer array nums, find the subarray with the largest sum and return the sum of the elements present in that subarray.
A subarray is a contiguous non-empty sequence of elements within an array.

Example 1 : Input: nums = [2, 3, 5, -2, 7, -4]
            Output: 15
            Explanation : The subarray from index 0 to index 4 has the largest sum = 15

Approach :
1. Consider every possible subarray.
2. For each starting index i, consider every ending index j.
3. Calculate the sum of the subarray arr[i...j] using a third loop.
4. Keep updating the maximum subarray sum found so far.
5. Return the maximum sum.

Time Complexity : O(n³)
Space Complexity : O(1)
"""
# Brute Force
class Solution:
    def maxSubArray(self,arr):
        maxi = float('-inf')
        n = len(arr)
        for i in range(n):
            for j in range(i,n):
                currentSum = 0
                for k in range(i,j+1):
                    currentSum += arr[k]
                    maxi = max(currentSum,maxi)
        return maxi
if __name__ == "__main__":
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    sol = Solution()
    print(sol.maxSubArray(arr))


# Better Approach
"""
Approach :
1. Iterate through each possible starting index i.
2. Initialize currentSum = 0.
3. Extend the subarray one element at a time by moving the ending index j.
4. Add arr[j] to currentSum.
5. Update the maximum subarray sum (maxi) after every extension.
6. Return maxi after checking all subarrays.

Time Complexity : O(n²)
Space Complexity : O(1)
"""
class Solution:
    def maxSubArray(self,arr):
        maxi = float('-inf')
        n = len(arr)
        for i in range(n):
            currentSum = 0
            for j in range(i,n):
                currentSum += arr[j]
                maxi = max(currentSum,maxi)
        return maxi
if __name__ == "__main__":
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    sol = Solution()
    print(sol.maxSubArray(arr))



# Optimal Solution
"""
Approach :
1. Initialize:
    currentSum = 0 to store the sum of the current subarray.
    maxi = -∞ to store the maximum subarray sum found so far.
2. Traverse the array from left to right.
3. Add the current element to currentSum.
4. Update maxi if currentSum is greater.
5. If currentSum becomes negative, reset it to 0 because a negative sum cannot help in forming a larger subarray in the future.
6. After the traversal, return maxi

Time Complexity : O(n)
Space Complexity : O(1)
"""
class Solution:
    def maxSubArray(self,arr):
        maxi = float('-inf')
        n = len(arr)
        currentSum = 0 
        for i in range(n):
            currentSum += arr[i]
            if currentSum > maxi:
                maxi = currentSum
            if currentSum < 0:
                currentSum = 0
        return maxi
if __name__ == "__main__":
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    sol = Solution()
    print(sol.maxSubArray(arr))


# Follow Up : Printing maxSubArray
"""
Approach :
1. Initialize:
    currentSum = 0
    maxi = -∞
2. Whenever currentSum == 0, record the current index as the possible start of a new subarray.
3. Add the current element to currentSum.
4. If currentSum is greater than maxi:
    Update maxi.
    Save start and the current index.
5. If currentSum becomes negative:
    Reset it to 0.
6. After traversal, print the subarray from ansStart to ansEnd.

Time Complexity : O(n)
Space Complexity : O(1)
"""
class Solution:
    def maxSubArray(self,arr):
        maxi = float('-inf')
        n = len(arr)
        currentSum = 0
        ansStart = -1
        ansEnd = -1
        for i in range(n):
            if currentSum == 0:
                start = i
            currentSum += arr[i]
            if currentSum > maxi:
                maxi = currentSum
                ansStart = start
                ansEnd = i
            if currentSum < 0:
                currentSum = 0
        print("The subarray is: [", end="")
        for i in range(ansStart, ansEnd + 1):
            print(arr[i], end=" ")
        print("]")
        return maxi
if __name__ == "__main__":
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    sol = Solution()
    print(sol.maxSubArray(arr))
