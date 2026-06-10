"""
Problem: Given a digit d (0 to 9), find the sum of the first 50 positive integers (integers > 0) that end with digit d.
         A number ends with digit d if its last digit is d.

Example 1 : Input: d = 1
            Output: 12300
            Explanation: The first 50 positive integers ending with 1 are: 1, 11, 21, 31, ..., 491
            Their sum is 12300.
Example 2 : Input: d = 5
            Output: 12500

Approach:
1. The numbers ending with digit d form an arithmetic sequence:
   d, d+10, d+20, d+30, ...
2. If d = 0, start from 10 because 0 is not a positive integer.
3. Initialize:
   - num as the first valid number ending with d
   - count = 0
   - total = 0
4. Use a while loop to process the first 50 numbers:
   - Add num to total
   - Increase num by 10
   - Increment count
5. Return the total sum after 50 iterations.

Time Complexity: O(1)
Space Complexity: O(1)
"""

class Solution:
    def whileLoop(self, d: int) -> int:
        count = 0
        num = d
        total = 0

        if d == 0:
            num = 10

        while count < 50:
            total += num
            num += 10
            count += 1

        return total

if __name__ == "__main__":
    sol = Solution()
    whileLoop = sol.whileLoop(7)
    print(whileLoop)