"""
Problem : Given an integer n. You need to recreate the pattern given below for any value of N. 
          Let's say for N = 5, the pattern should look like as below:
                                      **********
                                      ****  ****
                                      ***    ***
                                      **      **
                                      *        *
                                      *        *
                                      **      **
                                      ***    ***
                                      ****  ****
                                      **********

Print the pattern in the function given to you.

Approach : The pattern is formed in two parts:
            1. Upper Half
                Print n - i stars on the left.
                Print inis spaces in the middle.
                Print n - i stars on the right.
                Increase inis by 2 after each row.
            2. Lower Half
                Print i stars on the left.
                Print inis spaces in the middle.
                Print i stars on the right.
                Decrease inis by 2 after each row.
            This creates a symmetric hourglass/butterfly-shaped pattern.

Time Complexity : O(n²)
Space Complexity : O(1)
"""

class Solution:
    def pattern19(self,n):
        inis = 0
        for i in range(n):
            print("*" * (n-i),end="")
            print(" " * inis,end="")
            print("*" * (n-i))
            inis += 2
        inis = 2 * n - 2
        for i in range(1,n+1):
            print("*" * i,end="")
            print(" " * inis,end="")
            print("*" * i)
            inis -= 2
            

if __name__ == "__main__":
    sol = Solution()
    n = 5
    sol.pattern19(n)