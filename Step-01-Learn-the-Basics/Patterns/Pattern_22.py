"""
Problem : Given an integer n. You need to recreate the pattern given below for any value of N. 
          Let's say for N = 5, the pattern should look like as below:
                                      5 5 5 5 5 5 5 5 5 
                                      5 4 4 4 4 4 4 4 5 
                                      5 4 3 3 3 3 3 4 5 
                                      5 4 3 2 2 2 3 4 5 
                                      5 4 3 2 1 2 3 4 5 
                                      5 4 3 2 2 2 3 4 5 
                                      5 4 3 3 3 3 3 4 5 
                                      5 4 4 4 4 4 4 4 5 
                                      5 5 5 5 5 5 5 5 5

Print the pattern in the function given to you.

Approach :  This pattern is generated on a grid of size:
                        (2n-1)x(2n-1)
            For each cell (i, j):
                Compute its distance from all four boundaries:
                    Top = i
                    Left = j
                    Bottom = (2*n - 2) - i
                    Right = (2*n - 2) - j
                Find the minimum distance to any boundary:
                    minDist = min(top, bottom, left, right)
                The value to print is:
                    n - minDist

This creates concentric layers of numbers, decreasing toward the center.

Time Complexity : O(n²)
Space Complexity : O(1)
"""

class Solution:
    def pattern22(self, n):
        for i in range(2*n-1):
            for j in range(2*n-1):
                top = i
                left = j
                bottom = (2 * n -2) - i
                right = (2 * n - 2) - j
                minDist = min(top,bottom,right,left)
                print(n - minDist,end=" ")
            print()


if __name__ == "__main__":
    sol = Solution()
    n = 5
    sol.pattern22(n)
