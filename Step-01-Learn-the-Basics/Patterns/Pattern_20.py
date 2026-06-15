"""
Problem : Given an integer n. You need to recreate the pattern given below for any value of N. 
          Let's say for N = 5, the pattern should look like as below:
                                      *        *
                                      **      **
                                      ***    ***
                                      ****  ****
                                      **********
                                      ****  ****
                                      ***    ***
                                      **      **
                                      *        *

Print the pattern in the function given to you.

Approach :  This pattern is generated in a single loop.
            Initialize the middle spaces as:
                spaces=2n-2
            Iterate from 1 to 2n - 1.
            Determine the number of stars:
                For the first half (i ≤ n), stars increase from 1 to n.
                For the second half (i > n), stars decrease from n-1 to 1.
            // Code :
                    stars = i
                    if i > n:
                        stars = 2 * n - i
            Print:
                stars stars on the left.
                spaces spaces in the middle.
                stars stars on the right.
            Update the spaces:
                Decrease by 2 in the first half.
                Increase by 2 in the second half.

            This creates a symmetric butterfly shape.

Time Complexity : O(n²)
Space Complexity : O(1)
"""

class Solution:
    def pattern20(self, n):
        spaces = 2 * n - 2
        for i in range(1, 2 * n):
            stars = i
            if i > n:
                stars = 2 * n - i
            print("*" * stars, end="")
            print(" " * spaces, end="")
            print("*" * stars)
            if i < n:
                spaces -= 2
            else:
                spaces += 2


if __name__ == "__main__":
    sol = Solution()
    N = 5
    sol.pattern20(N)
