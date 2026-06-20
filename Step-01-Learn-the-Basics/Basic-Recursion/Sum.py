"""
Problem : Given an integer N, return the sum of first N natural numbers. Try to solve this using recursion.
          Example 1 : Input : N = 4
                      Output : 10
                      Explanation : first four natural numbers are 1, 2, 3, 4.
                      Sum is 1 + 2 + 3 + 4 => 10.


Approach :
1. Initialize sum = 0.
2. Iterate from 1 to n.
3. Add each number to sum.
4. After the loop ends, return the final sum.

Time Complexity : O(n)
Space Complexity : O(1)
"""
# Brute Force
class Solution:
    def NnumbersSum(self, n):
        sum = 0
        for i in range(1,n+1):
            sum += i
        return sum

if __name__ == "__main__":
    sol = Solution()
    n = 5
    total = sol.NnumbersSum(n)
    print(total)


# Using Formula

"""
Approach :
1. Multiply n by (n + 1).
2. Divide the result by 2.
3. Return the computed sum.

Time Complexity : O(1)
Space Complexity : O(1)


"""
class Solution:
    def NnumbersSum(self, n):
        return (n * (n+1))//2

if __name__ == "__main__":
    sol = Solution()
    n = 5
    print(sol.NnumbersSum(n))



# Recursive Approach
"""
Approach :
1. Define the base case:
    If n == 1, return 1.
2. For any other value of n, return:
    Current number n
3. Plus the sum of numbers from 1 to n-1.
4. The recursion continues until it reaches the base case.

Time Complexity : O(n)
Space Complexity : O(n)


"""
class Solution:
    def NnumbersSum(self, n):
        if n == 1:
            return 1
        return n + self.NnumbersSum(n-1)

if __name__ == "__main__":
    sol = Solution()
    n = 5
    print(sol.NnumbersSum(n))