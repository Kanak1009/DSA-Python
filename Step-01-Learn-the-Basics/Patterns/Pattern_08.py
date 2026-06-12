"""
Problem : Given an integer n. You need to recreate the pattern given below for any value of N. 
          Let's say for N = 5, the pattern should look like as below:

                                               *********
                                                *******
                                                 *****
                                                  ***
                                                   *
Print the pattern in the function given to you.

Approach :  Use an outer loop from n down to 1 to print each row.
            For each row i:
                Print n - i leading spaces.
                Print 2 * i - 1 stars.
            As i decreases, the number of stars decreases by 2 in each row.
            Continue until only one star remains.

Time Complexity : O(n²)
Space Complexity : O(1)
"""

class Solution:
    def pattern8(self, n):
        for i in range(n, 0, -1):

            # Print leading spaces
            for j in range(n - i):
                print(" ", end=" ")

            # Print stars
            for j in range(2 * i - 1):
                print("*", end=" ")

            print()

if __name__ == "__main__":
    sol = Solution()
    n = 5
    sol.pattern8(n)