"""
Problem : Given an integer n. You need to recreate the pattern given below for any value of N. 
          Let's say for N = 5, the pattern should look like as below:
                                    1
                                    12
                                    123
                                    1234
                                    12345
Print the pattern in the function given to you.

Approach :  Use an outer loop from 1 to n to represent the rows.
            For each row i, use an inner loop from 1 to i.
            Print the value of j in each iteration of the inner loop.
            Move to the next line after completing each row.


Time Complexity : O(n²)
Space Complexity : O(1)
"""

class Solution:
    def pattern3(self,n):
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                print(j, end=" ")
            print()

if __name__ == "__main__":
    sol = Solution()
    n = 5
    pattern3 = sol.pattern3(n)