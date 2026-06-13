"""
Problem : Given an integer n. You need to recreate the pattern given below for any value of N. 
          Let's say for N = 5, the pattern should look like as below:

                                               * 
                                              ***
                                             *****
                                            *******
                                           *********
                                           *********
                                            *******
                                             *****
                                              ***
                                               *
Print the pattern in the function given to you.

Approach :  Print a normal pyramid:
                Print n - i - 1 spaces.
                Print 2 * i + 1 stars.
            Print an inverted pyramid:
                Print n - i spaces.
                Print 2 * i - 1 stars.
            Combining both patterns creates a Diamond Pattern.

Time Complexity : O(n²)
Space Complexity : O(1)
"""

class Solution:
    def pattern9(self, n):
        for i in range(n):
            for j in range(n-i-1):
                print(" ",end="")
            for j in range(2*i+1):
                print("*",end="")
            print()

        for i in range(n,0,-1):
            for j in range(n-i):
                print(" ",end="")
            for j in range(2*i-1):
                print("*",end="")
            print()

if __name__ == "__main__":
    sol = Solution()
    n = 5
    sol.pattern9(n)