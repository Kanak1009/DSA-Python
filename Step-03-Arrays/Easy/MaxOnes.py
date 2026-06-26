"""
Problem :
Given a binary array nums, return the maximum number of consecutive 1s in the array.
A binary array is an array that contains only 0s and 1s.

Example 1 : Input: nums = [1, 1, 0, 0, 1, 1, 1, 0]
            Output: 3
            Explanation : The maximum consecutive 1s are present from index 4 to index 6, amounting to 3 1s


Approach :
1. Initialize:
    cnt = 0 to count consecutive 1s.
    maxi = 0 to store the maximum count.
2. Traverse the array from left to right.
3. If the current element is 1:
    Increment cnt.
    Update maxi.
4. If the current element is 0:
    Reset cnt to 0.
5. After the traversal, maxi contains the maximum number of consecutive 1s.

Time Complexity : O(n)
Space Complexity : O(1)
"""
class Solution:
    def maxOnes(self,arr):
        maxi = 0
        cnt = 0
        for i in range(1,len(arr)):
            if arr[i] == 1:
                cnt += 1
                maxi = max(maxi,cnt)
            else:
                cnt = 0
        return maxi

if __name__ == '__main__':
    arr = [1, 1, 0, 1, 1, 1]
    sol = Solution()
    print(sol.maxOnes(arr))