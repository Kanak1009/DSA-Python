"""
Problem :   You are given an integer n. You need to check whether the number is a palindrome number or not. 
            Return true if it's a palindrome number, otherwise return false.
            A palindrome number is a number which reads the same both left to right and right to left.

Example 1 : Input: n = 121
            Output: true
            Explanation: When read from left to right : 121.
            When read from right to left : 121.


Approach : 1. Store the original number in a separate variable (revNo).
           2. Reverse the number by:
                Extracting the last digit using % 10.
                Appending it to revNum.
                Removing the last digit using // 10.
           3. After the reversal is complete, compare the reversed number with the original number.
           4. If both are equal, the number is a palindrome; otherwise, it is not.

Time Complexity : O(log₁₀ n)
Space Complexity : O(1)
"""

class Solution:
    def palindromeNumber(self, n):
        original = n
        revNum = 0
        if n < 0:
            return False
        while n > 0:
            lastDigit = n % 10
            revNum = revNum * 10 + lastDigit
            n //= 10

        return original == revNum


if __name__ == "__main__":
    sol = Solution()
    print(sol.palindromeNumber(1223))