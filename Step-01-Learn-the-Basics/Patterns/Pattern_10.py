"""
Problem : Given an integer n. You need to recreate the pattern given below for any value of N. 
          Let's say for N = 5, the pattern should look like as below:
                                        *
                                        **
                                        ***
                                        ****
                                        *****
                                        ****
                                        ***
                                        **
                                        *
Print the pattern in the function given to you.


Approach : 1. Print an increasing triangle:
                For row i, print i + 1 stars.
                Print a decreasing triangle:
           2. Start from n - 1 stars and decrease to 1 star.
           3. Combining both triangles forms a symmetric pattern.

Time Complexity : O(n²)
Space Complexity : O(1)
"""

class Solution:
    def pattern10(self,n):
        for i in range(n):
            for j in range(i+1):
                print("*",end="")
            print()
        for i in range(n,0,-1):
            for j in range(i-1):
                print("*",end="")
            print()
if __name__ == "__main__":
    sol = Solution()
    n = 5
    sol.pattern10(n)