"""
Problem : Given an integer n. You need to recreate the pattern given below for any value of N. 
          Let's say for N = 5, the pattern should look like as below:
                                    1 
                                    2 3 
                                    4 5 6 
                                    7 8 9 10 
                                    11 12 13 14 15

Print the pattern in the function given to you.

Approach :  Initialize a variable num = 0 to keep track of the current number.
            Use an outer loop to iterate through the rows.
            For each row i, print i + 1 numbers using the inner loop.
            After printing a number, increment num by 1.
            Move to the next line after completing each row


Time Complexity : O(n²)
Space Complexity : O(1)
"""

class Solution:
    def pattern13(self,n):
        num = 0
        for i in range(n):
            for j in range(i+1):
                print(num+1, end=" ")
                num += 1
            print()

if __name__ == "__main__":
    sol = Solution()
    n = 5
    sol.pattern13(n)