"""
Problem :   You are given an integer n. You need to check whether it is an armstrong number or not. 
            Return true if it is an armstrong number, otherwise return false.
            An armstrong number is a number which is equal to the sum of the digits of the number, 
            raised to the power of the number of digits.

Example 1 : Input: n = 153
            Output: true
            Explanation: Number of digits : 3.
            13 + 53 + 33 = 1 + 125 + 27 = 153.
            Therefore, it is an Armstrong number.


Approach :  An Armstrong Number is a number that is equal to the sum of its digits each raised to the 
            power of the total number of digits.
            For a number n:
               1. Count the number of digits k.
               2. Store the original number.
               3. Extract each digit using % 10.
               4. Add digit^k to a running sum.
               5. Remove the last digit using // 10.
               6. After processing all digits, compare the sum with the original number.
               7. If they are equal, the number is an Armstrong number.

Time Complexity : O(log₁₀ n)
Space Complexity : O(log₁₀ n)
"""

class Solution:
    def armstrongNumber(self, n):
        k = len(str(n))
        sum = 0
        original = n
        while n > 0:
            lastDigit = n % 10
            sum += lastDigit **k
            n //= 10
        return sum == original

if __name__ == "__main__":
    sol = Solution()
    print(sol.armstrongNumber(164))