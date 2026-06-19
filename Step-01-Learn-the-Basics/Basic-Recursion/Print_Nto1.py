"""
Problem :
Given an integer n, write a function to print all numbers from n to 1 (inclusive) using recursion.
You must not use any loops such as for, while, or do-while.
The function should print each number on a separate line, in decreasing order from n to 1

Approach :
1. Start with the given number n.
2. Print the current number.
3. Recursively call the function with current - 1.
4. Continue until current < 1 (base case).
5. This prints numbers from n down to 1.

Time Complexity : O(N)
Space Complexity : O(N)

"""
# Forward Recursion
class Solution:
    def printNumbers(self, current):
        if current < 1:
            return

        print(current, end=' ')

        self.printNumbers(current - 1)

if __name__ == "__main__":
    sol = Solution()
    n = 10

    sol.printNumbers(n)
    print()




"""
Approach :
1. Start with the given number n.
2. Recursively call the function with current - 1 until current < 1.
3. Once the base case is reached, the recursion starts returning (backtracking).
4. Print the current number during the backtracking phase.
5. This results in numbers being printed from 1 to n.

Time Complexity : O(N)
Space Complexity : O(N)

"""
# Backtracking
class Solution:
    def printNumbers(self, current):
        if current < 1:
            return

        self.printNumbers(current - 1)

        print(current, end=' ')

if __name__ == "__main__":
    sol = Solution()
    n = 10

    sol.printNumbers(n)
    print()
