"""
Problem : Given an integer n, extract all its digits and return them in the same order as they appear in the number.

Approach : 1. Initialize an empty list ans.
           2. Repeatedly extract the last digit using:
                lastDigit = n % 10
           3. Append the extracted digit to the list.
           4. Remove the last digit from the number using:
                n = n // 10
           5. Continue until n becomes 0.
           6. Since digits are extracted from right to left, reverse the list to restore the original order.
           7. Return the list of digits.


Time Complexity : O(log₁₀ n)
Space Complexity : O(log₁₀ n)
"""

class Solution:
    def extractDigit(self, n):
        ans = []
        while n > 0:
            lastDigit = n % 10
            ans.append(lastDigit)
            n = n // 10
        ans.reverse()
        return ans
if __name__ == "__main__":
    sol = Solution()
    n = 778913
    digits = sol.extractDigit(n)
    print("Extracted Digits:", end=" ")
    for num in digits:
        print(num, end=" ")
    print()
