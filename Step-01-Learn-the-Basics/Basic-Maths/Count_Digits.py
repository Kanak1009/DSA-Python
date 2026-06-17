"""
Problem :   You are given an integer n. You need to return the number of digits in the number.
            The number will have no leading zeroes, except when the number is 0 itself.
Example 1 : Input: n = 4
            Output: 1

Explanation: There is only 1 digit in 4.

Example 2 : Input: n = 14
            Output: 2

Explanation: There are 2 digits in 14.

# Brute Force Approach
Approach :  Initialize a counter count = 0.
            Repeatedly remove the last digit of the number using integer division by 10:
                n = n // 10
            Increment count after each removal.
            Continue until n becomes 0.
            The final value of count is the number of digits.

Time Complexity : O(log₁₀ n)
Space Complexity : O(1)
"""

# Brute Force Approach
class Solution:
    def countDigit(self, n):
        count = 0
        while n > 0:
            count += 1
            n = n // 10
        print(count)
if __name__ == "__main__":
    sol = Solution()
    n = 778913
    sol.countDigit(n)

# Optimal Solution
"""
Approach :  Instead of repeatedly dividing the number by 10, use the mathematical property:
                    Number of Digits=⌊log10(n)⌋+1
            1. Compute log10(n).
            2. Take its integer part.
            3. Add 1 to get the total number of digits.

Time Complexity : O(1)
Space Complexity : O(1)
"""

import math
class Solution:
    def countDigit(self, n):
        cnt = int(math.log10(n) + 1)
        return cnt
if __name__ == "__main__":
    sol = Solution()
    n = 778913
    digits = sol.countDigit(n)
    print(digits)
    