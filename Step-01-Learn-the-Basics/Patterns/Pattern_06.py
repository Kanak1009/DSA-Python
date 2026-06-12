"""
Problem : Given an integer n. You need to recreate the pattern given below for any value of N. 
          Let's say for N = 5, the pattern should look like as below:
                                    12345
                                    1234
                                    123
                                    12
                                    1

Print the pattern in the function given to you.

Approach :  Use an outer loop from 1 to n to represent the rows.
            For each row i, print numbers from 1 to n - i + 1.
            As the row number increases, the count of printed numbers decreases by one.
            Move to the next line after each row.

Time Complexity : O(n²)
Space Complexity : O(1)
"""

class Solution:
    def pattern6(self,n):
        for i in range(1,n+1):
            for j in range(n-i+1):
                print(j+1,end=" ")
            print()

if __name__ == "__main__":
    sol = Solution()
    n = 5
    pattern6 = sol.pattern6(n)