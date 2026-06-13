"""
Problem : Given an integer n. You need to recreate the pattern given below for any value of N. ]
          Let's say for N = 5, the pattern should look like as below:
                                    1        1
                                    12      21
                                    123    321
                                    1234  4321
                                    1234554321


Print the pattern in the function given to you.



Approach :  Initialize spaces = 2 * (N - 1).
            For each row i from 1 to N:
            Print numbers from 1 to i (increasing order).
            Print the required number of spaces.
            Print numbers from i down to 1 (decreasing order).
            After each row, reduce the number of spaces by 2.
            Continue until the last row where no spaces remain.


Time Complexity : O(N²)
Space Complexity : O(1)
"""

class Solution:
    def pattern12(self, N):
        spaces = 2 * (N - 1)
        for i in range(1, N + 1):
            for j in range(1, i + 1):
                print(j, end="")
            for j in range(1, spaces + 1):
                print(" ", end="")
            for j in range(i, 0, -1):
                print(j, end="")
            print()
            spaces -= 2

if __name__ == "__main__":
    sol = Solution()
    N = 5
    sol.pattern12(N)