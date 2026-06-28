"""
Problem :
Given an array of integers nums and an integer target. Return the indices(0 - indexed) of two elements in nums such 
that they add up to target. Each input will have exactly one solution, and the same element cannot be used twice. 
Return the answer in any order.

Example 1 : Input: nums = [1, 6, 2, 10, 3], target = 7
            Output: [0, 1]
            Explanation : nums[0] + nums[1] = 1 + 6 = 7


Approach :
1. Traverse every possible pair of elements.
2. For each pair (i, j) where j > i:
    Compute arr[i] + arr[j].
3. If the sum equals the target:
    Return "YES" (Variant 1).
    Return [i, j] (Variant 2).
4. If no such pair exists after checking all pairs:
    Return "NO" or [-1, -1].

Time Complexity : O(n²)
Space Complexity : O(1)
"""
# Brute Force
class Solution:
    # Function to check if any two numbers sum up to target (variant 1)
    def two_sum_exists(self, arr, target):
        n = len(arr)
        for i in range(n):
            for j in range(i + 1, n):
                if arr[i] + arr[j] == target:
                    return "YES"
        return "NO"

    # Function to return indices of two numbers that sum to target (variant 2)
    def two_sum_indices(self, arr, target):
        n = len(arr)
        for i in range(n):
            for j in range(i + 1, n):
                if arr[i] + arr[j] == target:
                    return [i, j]
        return [-1, -1]

if __name__ == "__main__":
    sol = Solution()
    arr = [2, 6, 5, 8, 11]
    target = 14
    print(sol.two_sum_exists(arr, target))
    print(sol.two_sum_indices(arr, target))


# Better Approach : Hashing
"""
Approach :
1. Create an empty hash map mp.
2. Traverse the array once.
3. For each element:
    Compute its complement:
        complement = target - num
4. Check whether the complement already exists in the hash map.
    If yes, a valid pair has been found.
    If no, store the current element and its index in the hash map.
5. Continue until the array ends.

Time Complexity : O(n)
Space Complexity : O(n)
"""
class Solution:
    # Variant 1: Check if two numbers sum to target using hashing
    def two_sum_exists(self, arr, target):
        mp = {}
        for i, num in enumerate(arr):
            complement = target - num
            if complement in mp:
                return "YES"
            mp[num] = i
        return "NO"

    # Variant 2: Return indices of two numbers that sum to target using hashing
    def two_sum_indices(self, arr, target):
        mp = {}
        for i, num in enumerate(arr):
            complement = target - num
            if complement in mp:
                return [mp[complement], i]
            mp[num] = i
        return [-1, -1]

if __name__ == "__main__":
    sol = Solution()
    arr = [2, 6, 5, 8, 11]
    target = 14

    print(sol.two_sum_exists(arr, target))
    print(sol.two_sum_indices(arr, target))



# Optimal Solution : Two Pointers
"""
Approach :
1. Pair every element with its original index.
2. Sort the array based on the element values.
3. Initialize two pointers:
    left = 0
    right = n - 1
4.Compute the sum of the two pointed elements.
5. If:
    Sum equals target → return the answer.
    Sum is smaller → move left forward.
    Sum is larger → move right backward.
6. Continue until the pointers meet.

Time Complexity : O(n)
Space Complexity : O(1)
"""
class Solution:
    # Variant 1: Check if two numbers sum to target using two-pointer approach
    def two_sum_exists(self, arr, target):
        nums_with_index = [(num, idx) for idx, num in enumerate(arr)]
        nums_with_index.sort(key=lambda x: x[0])
        left, right = 0, len(arr) - 1
        while left < right:
            current_sum = nums_with_index[left][0] + nums_with_index[right][0]
            
            if current_sum == target:
                return "YES"
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        
        return "NO"

    # Variant 2: Return indices of two numbers that sum to target
    def two_sum_indices(self, arr, target):
        nums_with_index = [(num, idx) for idx, num in enumerate(arr)]

        nums_with_index.sort(key=lambda x: x[0])

        left, right = 0, len(arr) - 1
        
        while left < right:
            current_sum = nums_with_index[left][0] + nums_with_index[right][0]
            if current_sum == target:
                return [nums_with_index[left][1], nums_with_index[right][1]]
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        return [-1, -1]

if __name__ == "__main__":
    sol = Solution()
    arr = [2, 6, 5, 8, 11]
    target = 14

    print(sol.two_sum_exists(arr, target))
    print(sol.two_sum_indices(arr, target)) 

