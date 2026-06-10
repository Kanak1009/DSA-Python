"""
Problem: Given two integers low and high, return the sum of all integers from low to high inclusive.

Example 1 : Input: low = 1, high = 5
            Output: 15
            Explanation: 1 + 2 + 3 + 4 + 5 = 15
Example 2 : Input: low = 3, high = 7
            Output: 25
            Explanation: 3 + 4 + 5 + 6 + 7 = 25

Approach: Initialize a variable sum to 0.
          Iterate from low to high (inclusive) using a for loop.
          Add each number to sum.
          Return the final sum.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def ForLoop(self, low : int, high : int) -> int:
        sum = 0
        for i in range(low,high+1):
            sum += i
        return sum

if __name__ == "__main__":
    sol = Solution()
    loops = sol.ForLoop(3,7)
    print(loops)
