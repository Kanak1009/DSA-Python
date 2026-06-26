"""
Problem :
Given an integer array of size n containing distinct values in the range from 0 to n (inclusive), 
return the only number missing from the array within this range.

Example 1 : Input: nums = [0, 2, 3, 1, 4]
            Output: 5
            Explanation : nums contains 0, 1, 2, 3, 4 thus leaving 5 as the only missing number in the range [0, 5]

Approach :
1. Let N = len(arr) + 1, since one number is missing.
2. For every number from 1 to N:
    Search the entire array to check if the number exists.
3. If a number is not found, return it.
4. If every number is found, return -1 (this case generally won't occur for valid inputs).

Time Complexity : O(n²)
Space Complexity : O(1)
"""

# Brute Force : Linear Search
class Solution:
    def missingNum(self,arr):
        n = len(arr) + 1
    
        for i in range(1, n + 1):
            found = False
            for j in range(n - 1):
                if arr[j] == i:
                    found = True
                    break
            if not found:
                return i
        return -1

if __name__ == '__main__':
    arr = [8, 2, 4, 5, 3, 7, 1]
    sol = Solution()
    print(sol.missingNum(arr))


# Better Approach : Hashing
"""
Approach :
1. Let N = len(arr) + 1, since one number is missing.
2. Create a hash array of size N + 1 initialized with 0.
3. Traverse the input array and mark each number as present by incrementing its corresponding index in the hash array.
4.Traverse the hash array from 1 to N.
5. The index whose value is 0 represents the missing number.
6. Return the missing number.

Time Complexity : O(n)
Space Complexity : O(n)
"""
class Solution:
    def missingNum(self,arr):
        n = len(arr) + 1
        hash = [0] * (n + 1)
        for i in range(n - 1):
            hash[arr[i]] += 1

        for i in range(1, n + 1):
            if hash[i] == 0:
                return i
        return -1

if __name__ == '__main__':
    arr = [8, 2, 4, 5, 3, 7, 1]
    sol = Solution()
    print(sol.missingNum(arr))


# Optimal Solution 1 : Using Sum
"""
Approach :
1. Let N = len(arr) + 1, since exactly one number is missing.
2. Compute the expected sum of numbers from 1 to N using the formula:
3. Compute the actual sum of the array using sum(arr).
4. The difference between the expected sum and the actual sum is the missing number.
5. Return the result.

Time Complexity : O(n)
Space Complexity : O(1)
"""
class Solution:
    def missingNum(self,arr):
        n = len(arr) + 1
        totalSum = sum(arr)
        expSum = n * (n + 1) // 2
        return expSum - totalSum

if __name__ == '__main__':
    arr = [8, 2, 4, 5, 3, 7, 1]
    sol = Solution()
    print(sol.missingNum(arr))

# Optimal Solution 1 : Using XOR
"""
Approach :
1. Let N = len(arr) + 1.
2. Compute the XOR of all numbers from 1 to N and store it in xor1.
3. Compute the XOR of all elements in the array and store it in xor2.
4. XOR xor1 and xor2.
5. Since every common number cancels out (x ^ x = 0), the remaining value is the missing number.

Time Complexity : O(n)
Space Complexity : O(1)
"""
class Solution:
    def missingNum(self,arr):
        n = len(arr) + 1
        xor1 = 0
        xor2 = 0
        for i in range(n - 1):
            xor2 ^= arr[i]
        for i in range(1, n + 1):
            xor1 ^= i
        return xor1 ^ xor2

if __name__ == '__main__':
    arr = [8, 2, 4, 5, 3, 7, 1]
    sol = Solution()
    print(sol.missingNum(arr))