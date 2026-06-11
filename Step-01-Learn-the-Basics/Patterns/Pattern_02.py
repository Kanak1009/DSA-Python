"""
Problem : Given an integer n. You need to recreate the pattern given below for any value of N. 
          Let's say for N = 5, the pattern should look like as below:
                                    *
                                    **
                                    ***
                                    ****
                                    *****
Print the pattern in the function given to you.

Approach :  Use an outer loop from 1 to n+1 to represent the rows.
            For each row i, print i stars using an inner loop.
            After printing the stars for a row, move to the next line.

Time Complexity :O(n²)
Space Complexity :O(1)
"""

class Solution:
    def pattern2(self,n):
        for i in range(1,n+1):
            for j in range(i):
                print("*",end=" ")
            print()

if __name__ == "__main__":
    sol = Solution()
    n = 5
    pattern2 = sol.pattern2(n)