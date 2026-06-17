"""
Problem : You are given an integer n. Return the integer formed by placing the digits of n in reverse order.
          Note: If a number has trailing zeros, then its reverse will not include them. 
          For e.g , reverse of 10400 will be 401 instead of 00401.
Example 1 : Input: n = 25
            Output: 52
            Explanation: Reverse of 25 is 52.


Approach :  1. Initialize revNum = 0.
            2. Extract the last digit of the number using:
                lastDigit = n % 10
            3. Append this digit to the reversed number:
                revNum = revNum * 10 + lastDigit
            4. Remove the last digit from the original number:
                n = n // 10
            5. Repeat until n becomes 0.
            6. Return revNum.


Time Complexity : O(log₁₀ n)
Space Complexity : O(1)
"""

class Solution:
    def reverseNumber(self,n):
        revNum = 0
        while n > 0:
            lastDigit = n % 10
            revNum = revNum * 10 + lastDigit
            n = n // 10
        return revNum

if __name__ == "__main__":
    sol = Solution()
    n = 123
    print(sol.reverseNumber(n))