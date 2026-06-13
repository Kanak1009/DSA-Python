"""
Problem : Given an integer n. You need to recreate the pattern given below for any value of N. 
          Let's say for N = 5, the pattern should look like as below:
                                        1 
                                        0 1 
                                        1 0 1 
                                        0 1 0 1 
                                        1 0 1 0 1

Print the pattern in the function given to you.

Approach :  Iterate through each row using the outer loop.
            Determine the starting value:
                If the row index i is even, start with 1.
                If the row index i is odd, start with 0.
            Print i + 1 elements in the current row.
            After printing each element, toggle the value using:
                start = 1 - start
            This switches:
            1 → 0
            0 → 1
            Repeat for all rows.


Time Complexity : O(n²)
Space Complexity : O(1)
"""

class Solution:
    def pattern11(self,n):
        for i in range(n):
            if i % 2 == 0:
                start = 1
            else:
                start = 0
            for j in range(i+1):
                print(start,end="")
                start = 1 - start
            print()

if __name__ == "__main__":
    sol = Solution()
    n = 5
    sol.pattern11(n)