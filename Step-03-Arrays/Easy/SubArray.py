"""
Problem :
Given an array nums of size n and an integer k, find the length of the longest sub-array that sums to k. 
If no such sub-array exists, return 0.


Example 1 : Input: nums = [10, 5, 2, 7, 1, 9],  k=15
            Output: 4
            Explanation : The longest sub-array with a sum equal to 15 is [5, 2, 7, 1], which has a length of 4. 
            This sub-array starts at index 1 and ends at index 4, and the sum of its elements (5 + 2 + 7 + 1) equals 15. 
            Therefore, the length of this sub-array is 4.


Approach :
1. Consider every possible subarray.
2. For each starting index:
3. Consider every possible ending index.
4. Compute the sum of the current subarray by traversing it.
5. If the sum equals k, update the maximum length.
6. Return the maximum length after checking all subarrays.

Time Complexity : O(n³)
Space Complexity : O(1)
"""

class Solution:
    def longestSubArray(self,arr,k):
        n = len(arr) 
        maxLength = 0
        for startIndex in range(n):
            for endIndex in range(startIndex, n):
                currentSum = 0
                for i in range(startIndex, endIndex + 1):
                    currentSum += arr[i]

                if currentSum == k:
                    maxLength = max(maxLength, endIndex - startIndex + 1)

        return maxLength
    
if __name__ == "__main__":
    arr = [10, 5, 2, 7, 1, 9]
    k = 15
    sol = Solution()
    print(sol.longestSubArray(arr,k))


# Better Approach : Hashing
"""
Approach :
1. Maintain a running prefix sum while traversing the array.
2. If the current prefix sum equals k, then the subarray from index 0 to i has sum k.
3. Otherwise, compute:
    remaining = prefix_sum - k
4. If remaining has been seen before, then the subarray between the previous index and the current index sums to k.
5. Store the first occurrence of every prefix sum in a hash map.
6. Keep updating the maximum subarray length.

Time Complexity : O(n)
Space Complexity : O(n)
"""
class Solution:
    def longestSubArrayWithSumK(self, arr, k):
        preSumMap = {}
        prefix_sum = 0
        maxLen = 0
        for i in range(len(arr)):
            prefix_sum += arr[i]
            if prefix_sum == k:
                maxLen = max(maxLen, i + 1)

            rem = prefix_sum - k
            if rem in preSumMap:
                length = i - preSumMap[rem]
                maxLen = max(maxLen, length)
            if prefix_sum not in preSumMap:
                preSumMap[prefix_sum] = i

        return maxLen

if __name__ == "__main__":
    arr = [10, 5, 2, 7, 1, 9]
    k = 15

    sol = Solution()
    print(sol.longestSubArrayWithSumK(arr, k))


# Optimal Solution : Two Pointers
"""
Approach :
1. Initialize two pointers:
    left = 0
    right = 0
2. Maintain the sum of the current window (currentSum).
3. Expand the window by moving right.
4. If currentSum becomes greater than k, shrink the window by moving left until currentSum <= k.
5. Whenever currentSum == k, update the maximum length.
6. Continue until right reaches the end of the array.

Time Complexity : O(n)
Space Complexity : O(n)
"""
class Solution:
    def longestSubArrayWithSumK(self, arr, k):
        left, right = 0, 0
        maxLen = 0
        currentSum = arr[0]
        n = len(arr)
        while right < n:
            while left <= right and currentSum > k:
                currentSum -= arr[left]
                left += 1
            if currentSum == k:
                maxLen = max(maxLen, right - left + 1)
            right += 1
            if right < n:
                currentSum += arr[right]
        return maxLen

if __name__ == "__main__":
    arr = [10, 5, 2, 7, 1, 9]
    k = 15

    sol = Solution()
    print(sol.longestSubArrayWithSumK(arr, k))