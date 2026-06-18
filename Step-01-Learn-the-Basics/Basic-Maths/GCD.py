"""
Problem :   You are given two integers n1 and n2. You need find the Greatest Common Divisor (GCD) of the two given numbers. 
            Return the GCD of the two numbers.
            The Greatest Common Divisor (GCD) of two integers is the largest positive integer that divides both of the integers.

Example 1 : Input: n1 = 4, n2 = 6
            Output: 2
            Explanation: Divisors of n1 = 1, 2, 4, Divisors of n2 = 1, 2, 3, 6
            Greatest Common divisor = 2.

# Brute Force
Approach : 1. Initialize gcd = 1.
           2. Iterate from 1 to min(n1, n2).
           3. For each number i, check whether it divides both n1 and n2:
                if (n1 % i == 0) and (n2 % i == 0):
           4. If it does, update gcd = i.
           5. After the loop finishes, gcd will contain the largest common divisor.

Time Complexity : O(min(n1, n2))
Space Complexity : O(1)
"""

# Brute Force 
class Solution:
    def GCD(self, n1, n2):
        gcd = 1
        for i in range(1,min(n1,n2)+1):
            if (n1 % i == 0) and (n2 % i == 0):
                gcd = i
        return gcd

if __name__ == "__main__":
    sol = Solution()
    n1,n2 = 5 , 10
    gcd = sol.GCD(n1,n2)
    print("GCD of", n1, "and", n2, "is:", gcd)


# Better Approach
"""
Approach : 1. Start checking from the smaller of the two numbers:
                min(n1, n2)
           2. Iterate backwards down to 1.
           3. For each number i, check if it divides both n1 and n2.
           4. The first common divisor encountered will be the greatest common divisor, so return it immediately.
           5. If no larger common divisor is found, return 1.

Time Complexity : O(min(n1, n2))
Space Complexity : O(1)

"""
class Solution:
    def GCD(self, n1, n2):
        gcd = 1
        for i in range(min(n1,n2),0,-1):
            if (n1 % i == 0) and (n2 % i == 0):
                return i
        return 1

if __name__ == "__main__":
    sol = Solution()
    n1,n2 = 5 , 10
    gcd = sol.GCD(n1,n2)
    print("GCD of", n1, "and", n2, "is:", gcd)


# Optimal Approach
"""
Approach :  The Euclidean Algorithm is based on the property:
                gcd(a,b)=gcd(a mod b,b)
           1. While both numbers are greater than 0:
           2. If a > b, replace a with a % b.
           3. Otherwise, replace b with b % a.
           4. One of the numbers will eventually become 0.
           5. The other non-zero number is the GCD.
           6. Return the non-zero value.

Time Complexity : O(log(min(a, b)))
Space Complexity : O(1)

"""
class Solution:
    def GCD(self, a, b):
        while a > 0 and b > 0:
            if a > b:
                a %= b
            else:
                b %= a
        if a == 0:
            return b
        return a

if __name__ == "__main__":
    sol = Solution()
    n1,n2 = 5 , 10
    gcd = sol.GCD(n1,n2)
    print("GCD of", n1, "and", n2, "is:", gcd)