"""
Problem :   You are given an integer n. You need to find all the divisors of n. 
            Return all the divisors of n as an array or list in a sorted order.
            A number which completely divides another number is called it's divisor.

Example 1 : Input: n = 6
            Output = [1, 2, 3, 6]
            Explanation: The divisors of 6 are 1, 2, 3, 6.


Approach :  1. Initialize an empty list res.
            2. Iterate from 1 to n.
            3. For each number i, check if it divides n exactly:
                    if n % i == 0:
            4. If yes, add i to the result list.
            5. After the loop ends, return all divisors.

Time Complexity : O(n)
Space Complexity : O(n)
"""

# Brute Force 
class Solution:
    def divisors(self, n):
        res = []
        for i in range(1,n+1):
            if n % i == 0:
                res.append(i)
        return res

if __name__ == "__main__":
    sol = Solution()
    n = 36
    result = sol.divisors(n)
    print("Divisors of", n, ":", *result)


# Optimal Approach
"""
Approach :  1. Observe that divisors always occur in pairs.
                If i divides n, then n // i is also a divisor.
            2. Iterate only from 1 to √n using math.isqrt(n).
            3. For every divisor i:
                Add i to the result.
                Add n // i if it is different from i (to avoid duplicates for perfect squares).
            4. Sort the result list before returning because divisors are collected in arbitrary order.

Time Complexity : O(√n)
Space Complexity : O(d)

"""
import math
class Solution:
    def divisors(self, n):
        res = []
        for i in range(1,int(math.isqrt(n))+1):
            if n % i == 0:
                res.append(i)
                
                if i != n // i:
                    res.append(n // i)
        return sorted(res)

if __name__ == "__main__":
    sol = Solution()
    n = 36
    result = sol.divisors(n)
    print("Divisors of", n, ":", *result)