"""
Problem: Given an integer n. You need to recreate the pattern given below for any value of N. 
         Let's say for N = 5, the pattern should look like as below:
                                    *****
                                    *****
                                    *****
                                    *****
                                    *****
Print the pattern in the function given to you.

Example 1 : Input: n = 4
Output:
*****
*****
*****
*****
Example 2 : Input: n = 2
Output:
*****
*****

Approach :  Use an outer loop to print n rows.
            For each row, use an inner loop to print n stars (*).
            After printing one row, move to the next line using print().

Time Complexity: O(n²)
Space Complexity: O(1)
"""

class Solution:
    def pattern1(self,n):
        for i in range(n):
            for j in range(n):
                print("*",end="")
            print()

if __name__ == "__main__":
    sol = Solution()
    pattern1 = sol.pattern1(5)