"""
Problem :
Given an array of nums of n integers. Every integer in the array appears twice except one integer. 
Find the number that appeared once in the array.

Example 1 : Input : nums = [1, 2, 2, 4, 3, 1, 4]
            Output : 3
            Explanation : The integer 3 has appeared only once.

Approach :
1. Traverse each element in the array.
2. For every element, count how many times it appears by scanning the entire array again.
3. If the count is 1, return that element.
4. If no such element exists, return -1.

Time Complexity : O(n²)
Space Complexity : O(1)
"""
# Brute Force
class Solution:
    def singleNumber(self,arr):
        n = len(arr)
        for i in range(n):
            num = arr[i]
            count = 0
            for j in range(n):
                if arr[j] == num:
                    count += 1
            if count == 1:
                return num

        return -1

if __name__ == '__main__':
    arr = [4, 1, 2, 1, 2]
    sol = Solution()
    print(sol.singleNumber(arr))


# Better Approach
"""
Approach :
1. Find the maximum element in the array.
2. Create a hash array of size max_element + 1.
3. Traverse the array and increment the frequency of each element.
4. Traverse the array again.
5. The first element whose frequency is 1 is the required answer.
6. Return that element.

Time Complexity : O(n)
Space Complexity : O(max(arr))
"""
class Solution:
    def singleNumber(self,arr):
        n = len(arr)
        maxi = max(arr)
        hash_arr = [0] * (maxi + 1)
        for num in arr:
            hash_arr[num] += 1
        for num in arr:
            if hash_arr[num] == 1:
                return num

        return -1

if __name__ == '__main__':
    arr = [4, 1, 2, 1, 2]
    sol = Solution()
    print(sol.singleNumber(arr))


# Optimal Approach
"""
Approach :
1. Initialize a variable xorr = 0.
2. Traverse the array.
3. XOR every element with xorr.
4. Since every element except one appears exactly twice:
    Equal elements cancel each other out (a ^ a = 0).
    0 ^ x = x
5. The remaining value after all XOR operations is the element that appears only once.

Time Complexity : O(n)
Space Complexity : O(1)
"""
class Solution:
    def singleNumber(self,arr):
        xorr = 0
        for num in arr:
            xorr ^= num

        return xorr

if __name__ == '__main__':
    arr = [4, 1, 2, 1, 2]
    sol = Solution()
    print(sol.singleNumber(arr))