"""
Problem : Given an integer n. You need to recreate the pattern given below for any value of N. 
          Let's say for N = 5, the pattern should look like as below:

                                                *
                                               ***
                                              *****
                                             *******
                                            *********
Print the pattern in the function given to you.

Approach :  Use an outer loop from 1 to n to print each row.
            For each row i:
            Print n - i leading spaces to center the pyramid.
            Print 2*i - 1 stars to form the pyramid shape.
            Move to the next line after each row.

Time Complexity : O(n²)
Space Complexity : O(1)
"""

class Solution:
    def pattern7(self, n):
        for i in range(n):

            # Print leading spaces
            for j in range(n - i - 1):
                print(" ", end="")

            # Print stars
            for j in range(2 * i + 1):
                print("*", end="")

            print()

if __name__ == "__main__":
    sol = Solution()
    n = 5
    sol.pattern7(n)