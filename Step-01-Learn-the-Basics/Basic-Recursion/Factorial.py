"""
Problem : You are given an integer n. Return the value of n! or n factorial.
          Factorial of a number is the product of all positive integers less than or equal to that number.
          Example 1 :   Input: n = 2
                        Output: 2
                        Explanation: 2! = 1 * 2 = 2.


Approach :
1. Initialize fact = 1.
2. Iterate from 1 to n.
3. Multiply fact by the current number in each iteration.
4. After the loop completes, fact contains the factorial of n.
5. Return fact.

Time Complexity : O(n)
Space Complexity : O(1)
"""
# Iterative Approach
class Solution:
    def factorial(self, n):
        fact = 1
        for i in range(1,n+1):
            fact *= i
        return fact

if __name__ == "__main__":
    sol = Solution()
    n = 5
    factorial = sol.factorial(n)
    print(factorial)


# Recursive Approach
""" 
Approach :
1.Define the base case:
    If n == 0 or n == 1, return 1.
2. For any other value of n, return:
    n x factorial(n - 1)
3. The recursion continues until it reaches the base case.
4. During backtracking, the multiplications are performed to compute the factorial.
The recurrence relation is:
            fact(n)=n×fact(n−1)
with:
            fact(0)=fact(1)=1


Time Complexity : O(n)
Space Complexity : O(n)

"""
class Solution:
    def factorial(self, n):
        fact = 1
        for i in range(1,n+1):
            fact *= i
        return fact

if __name__ == "__main__":
    sol = Solution()
    n = 5
    factorial = sol.factorial(n)
    print(factorial)