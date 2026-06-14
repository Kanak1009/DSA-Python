"""
Problem : Given an integer n. You need to recreate the pattern given below for any value of N. 
          Let's say for N = 5, the pattern should look like as below:
                                    A
                                    BB
                                    CCC
                                    DDDD
                                    EEEEE

Print the pattern in the function given to you.

Approach :  Use an outer loop from 0 to n - 1 to represent the rows.
            For each row i, print the character corresponding to chr(65 + i).
            Print that character i + 1 times using the inner loop.
            Move to the next line after completing each row.

Time Complexity : O(n²)
Space Complexity : O(1)
"""

class Solution:
    def pattern16(self,n):
        for i in range(n):
            for j in range(i+1):
                print(chr(65+i), end="")
            print()

if __name__ == "__main__":
    sol = Solution()
    n = 5
    sol.pattern16(n)