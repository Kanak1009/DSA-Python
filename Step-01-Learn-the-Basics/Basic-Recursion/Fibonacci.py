"""
Problem :
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, 
such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
    F(0) = 0, F(1) = 1
    F(n) = F(n - 1) + F(n - 2), for n > 1.


Approach :
1. Handle the base cases:
    If n == 0, print 0.
    If n == 1, print 0 1.
2. Create an array fib of size n + 1.
3. Initialize:
    fib[0] = 0
    fib[1] = 1
4. Iterate from 2 to n:
    Compute each Fibonacci number using:
        fib[i] = fib[i - 1] + fib[i - 2]
5. Print the Fibonacci sequence.

Time Complexity : O(n)
Space Complexity : O(n)
"""
# Brute Force Approach
class Solution:
    def fib(self, n):
        if n == 0:
            print("0")
        elif n == 1:
            print("0 1")
        else:
            fib = [0] * (n + 1)
            fib[0] = 0
            fib[1] = 1
            
            for i in range(2,n+1):
                fib[i] = fib[i - 1] + fib[i - 2]
            print(f"The Fibonacci Series up to {n}th term:")
            print(" ".join(str(num) for num in fib))
if __name__ == "__main__":
    sol = Solution()
    n = 5
    sol.fib(n)


# Better Approach
""" 
Approach :
1. Handle the special case when n = 0.
2. Initialize:
    second_last = 0
    last = 1
3. Print the first two Fibonacci numbers.
4. Iterate from 2 to n:
    Compute the current Fibonacci number:
        cur = second_last + last
    Update:
        second_last = last
        last = cur
5. Print each newly generated Fibonacci number.


Time Complexity : O(n)
Space Complexity : O(1)

"""
class Solution:
    def fib(self, n):
        if n == 0:
            print(f"The Fibonacci Series up to {n}th term:")
            print(0)
        else:
            second_last = 0 
            last = 1

            print(f"The Fibonacci Series up to {n}th term:")
            print(f"{second_last} {last}", end=" ")
    
            for i in range(2, n + 1):
                cur = last + second_last
                second_last = last
                last = cur
                print(cur, end=" ")
            
if __name__ == "__main__":
    sol = Solution()
    n = 5
    sol.fib(n)


# Optimal Approach (Recursion)
""" 
Approach :
1. Define the base cases:
    If n <= 1, return n.
2. For any other value of n, recursively compute:
    fib(n - 1)
    fib(n - 2)
3. Return their sum.
The recurrence relation is:
    fib(n) = fib(n-1) + fib(n-2)
with:
    fib(0) = 0
    fib(1) = 1


Time Complexity : O(2ⁿ)
Space Complexity : O(n)

"""
class Solution:
    def fib(self, n):
        if n <= 1:
            return n
        last = self.fib(n - 1)
        slast = self.fib(n - 2)

        return last + slast
            
if __name__ == "__main__":
    sol = Solution()
    n = 6
    print(sol.fib(n))