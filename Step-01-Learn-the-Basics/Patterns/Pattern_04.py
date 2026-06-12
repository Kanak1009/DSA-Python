"""
Problem : Given an integer n. You need to recreate the pattern given below for any value of N. 
          Let's say for N = 5, the pattern should look like as below:
                                    1
                                    22
                                    333
                                    4444
                                    55555

Print the pattern in the function given to you.

Approach :  Use an outer loop from 1 to n to represent the rows.
            For each row i, run an inner loop i times.
            Print the current row number i during each iteration of the inner loop.
            Move to the next line after completing each row.


Time Complexity : O(n²)
Space Complexity : O(1)
"""

class Solution:
    def pattern4(self,n):
        for i in range(1, n+1):
            for j in range(1,i + 1):
                print(i, end=" ")
            print()

if __name__ == "__main__":
    sol = Solution()
    n = 5
    pattern4 = sol.pattern4(n)