"""
Problem :   You are given an integer n. You need to check if the number is prime or not. 
            Return true if it is a prime number, otherwise return false.
            A prime number is a number which has no divisors except 1 and itself.
Example 1 : Input: n = 5
            Output: true
            Explanation: The only divisors of 5 are 1 and 5 , So the number 5 is prime.

# Brute Force
Approach :  Initialize a counter cnt = 0.
            Iterate from 1 to n.
            For each number i, check if it divides n exactly:
                if n % i == 0:
                    cnt += 1
            A prime number has exactly 2 divisors:
                1
                The number itself
            Return True if cnt == 2, otherwise return False.

Time Complexity : O(n)
Space Complexity : O(1)
"""

# Brute Force 
class Solution:
    def checkPrime(self,n):
        cnt = 0  
        for i in range(1, n + 1):
            if n % i == 0:
                cnt += 1
        return cnt == 2

if __name__ == "__main__":
    sol = Solution()
    n = 1483
    isPrime = sol.checkPrime(n) 
    if isPrime:
        print(f"{n} is a prime number.")
    else:
        print(f"{n} is not a prime number.")


# Optimal Approach
"""
Approach :  1. A prime number is a number greater than 1 that has exactly two divisors: 1 and itself.
            2. Handle the edge case:
                    If n <= 1, return False.
            3. Check for divisors only from 2 to √n.
            4. If any number divides n exactly, return False.
            5. If no divisor is found, return True.

Time Complexity : O(√n)
Space Complexity : O(1)

"""
import math
class Solution:
    def checkPrime(self, n):
        if n <= 1:
            return False

        for i in range(2, math.isqrt(n) + 1):
            if n % i == 0:
                 return False

        return True

if __name__ == "__main__":
    sol = Solution()
    n = 5
    isPrime = sol.checkPrime(n) 
    if isPrime:
        print(f"{n} is a prime number.")
    else:
        print(f"{n} is not a prime number.")