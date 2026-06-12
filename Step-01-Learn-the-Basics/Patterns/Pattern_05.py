"""
Problem : Given an integer n. You need to recreate the pattern given below for any value of N. 
          Let's say for N = 5, the pattern should look like as below:
                                    *****
                                    ****
                                    ***
                                    **
                                    *

Print the pattern in the function given to you.

Approach :  Use an outer loop from 1 to n to represent the rows.
            For each row i, print n - i + 1 stars.
            As i increases, the number of stars decreases by one in each row.
            Move to the next line after completing each row.

Time Complexity : O(n²)
Space Complexity : O(1)
"""

class Solution:
    def pattern5(self,n):
        for i in range(1,n+1):
            for j in range(n-i+1):
                print("*",end=" ")
            print()

if __name__ == "__main__":
    sol = Solution()
    n = 5
    pattern5 = sol.pattern5(n)