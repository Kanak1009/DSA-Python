"""
Problem : Given an integer n. You need to recreate the pattern given below for any value of N. 
          Let's say for N = 5, the pattern should look like as below:
                                    ABCDE
                                    ABCD
                                    ABC
                                    AB
                                    A

Print the pattern in the function given to you.

Approach :  Use an outer loop to iterate through the rows (0 to n-1).
            For each row i, print the first n - i uppercase alphabets.
            Convert the index j to its corresponding character using:
                chr(65 + j)
            As i increases, the number of characters printed decreases by one.
            Move to the next line after each row.

Time Complexity : O(n²)
Space Complexity : O(1)
"""

class Solution:
    def pattern15(self,n):
        for i in range(n):
            for j in range(n-i):
                print(chr(65+j), end="")
            print()

if __name__ == "__main__":
    sol = Solution()
    n = 5
    sol.pattern15(n)