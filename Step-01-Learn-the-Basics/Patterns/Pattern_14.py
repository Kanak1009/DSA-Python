"""
Problem : Given an integer n. You need to recreate the pattern given below for any value of N. 
          Let's say for N = 5, the pattern should look like as below:
                                    A
                                    AB
                                    ABC
                                    ABCD
                                    ABCDE

Print the pattern in the function given to you.

Approach :  Use an outer loop to iterate through the rows (0 to n-1).
            For each row i, use an inner loop to print the first i + 1 uppercase alphabets.
            Convert numbers to characters using:
                chr(65 + j)
            where:
                65 is the ASCII value of 'A'
                66 → 'B'
                67 → 'C', and so on.
            Move to the next line after each row.

Time Complexity : O(n²)
Space Complexity : O(1)
"""

class Solution:
    def pattern14(self,n):
        for i in range(n):
            for j in range(i+1):
                print(chr(65+j), end="")
            print()

if __name__ == "__main__":
    sol = Solution()
    n = 5
    sol.pattern14(n)