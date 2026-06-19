"""
Problem :
Given an integer n, write a function to print all numbers from 1 to n (inclusive) using recursion.
You must not use any loops such as for, while, or do-while.
The function should print each number on a separate line, in increasing order from 1 to n.

Approach :
1. Start with current = 1.
2. Print the current number.
3. Recursively call the function with current + 1.
4. Stop the recursion when current > n (base case).
This prints numbers from 1 to n in increasing order.

Time Complexity : O(N)
Space Complexity : O(N)

"""
# Forward Recursion
class Solution:
    def printNumbers(self, current, n):
        if current > n:
            return

        print(current, end=' ')

        self.printNumbers(current + 1, n)


if __name__ == "__main__":
    sol = Solution()
    n = 10

    sol.printNumbers(1, n)
    print()



"""
Approach :
1. Start with current = 1.
2. Instead of printing immediately, first make a recursive call with current + 1.
3. Continue until current > n (base case).
4. As the recursive calls return (backtracking phase), print the current number.
5. Since printing happens while returning from recursion, the numbers are printed in reverse order.

Time Complexity : O(N)
Space Complexity : O(N)

"""
# Backtracking
class Solution:
    def printNumbers(self, current, n):
        if current > n:
            return

        self.printNumbers(current + 1, n)

        print(current, end=' ')


if __name__ == "__main__":
    sol = Solution()
    n = 10

    sol.printNumbers(1, n)
    print()
