"""
Problem : Given an integer n. You need to recreate the pattern given below for any value of N. 
          Let's say for N = 5, the pattern should look like as below:
                                      A
                                     ABA
                                    ABCBA
                                   ABCDCBA
                                  ABCDEDCBA

Print the pattern in the function given to you.

Approach :  Use an outer loop to iterate through each row.
            Print the required leading spaces (n - i - 1) to center the pattern.
            Start with the character 'A'.
            Calculate the middle position:
                breakpoint = 2i+1 / 2
            Print characters:
                Increase the character from A → B → C → ... until the middle.
                Then decrease the character symmetrically back to A.
            Move to the next line after each row.

Time Complexity : O(n²)
Space Complexity : O(1)
"""

class Solution:
    def pattern17(self,n):
        for i in range(n):
            print(" " * (n - i - 1), end="")
            ch = ord('A')
            breakpoint = (2 * i + 1) // 2
            for j in range(1,2*i+2):
                print(chr(ch),end="")
                if j <= breakpoint:
                    ch += 1
                else :
                    ch -= 1
            print()

if __name__ == "__main__":
    sol = Solution()
    n = 5
    sol.pattern17(n)