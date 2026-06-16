"""
Problem : Given an integer n. You need to recreate the pattern given below for any value of N. 
          Let's say for N = 5, the pattern should look like as below:
                                      *****
                                      *   *
                                      *   *
                                      *   *
                                      *****

Print the pattern in the function given to you.

Approach :  Use two nested loops to traverse every position in an n × n grid.
            For each position (i, j):
                Print * if it lies on the border:
                    First row (i == 0)
                    Last row (i == n - 1)
                    First column (j == 0)
                    Last column (j == n - 1)
                Otherwise, print a space " ".
            Move to the next line after completing each row.

Time Complexity : O(n²)
Space Complexity : O(1)
"""

class Solution:
    def pattern21(self, n):
        for i in range(n):
            for j in range(n):
                if i == 0 or j == 0 or i == n-1 or j == n-1:
                    print("*",end="")
                else:
                    print(" ",end="")
            print()


if __name__ == "__main__":
    sol = Solution()
    n = 5
    sol.pattern21(n)
