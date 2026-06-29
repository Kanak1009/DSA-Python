"""
Problem :
Given an array arr of n integers, where arr[i] represents price of the stock on the ith day. 
Determine the maximum profit achievable by buying and selling the stock at most once. 
The stock should be purchased before selling it, and both actions cannot occur on the same day.

Example 1 : Input: arr = [10, 7, 5, 8, 11, 9]
            Output: 6
            Explanation: Buy on day 3 (price = 5) and sell on day 5 (price = 11), profit = 11 - 5 = 6.

Approach :
1. Consider every possible buying day i.
2. For each buying day, consider every possible selling day j where j > i.
3. Compute the profit:
    profit = prices[j] - prices[i]
4. Update the maximum profit.
5. Return the maximum profit.

Time Complexity : O(n²)
Space Complexity : O(1)
"""
# Brute Force
class Solution:
    def stockBuySell(self, prices):
        maxProfit = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                profit = prices[j] - prices[i]
                maxProfit = max(maxProfit, profit)
        return maxProfit

if __name__ == "__main__":
    sol = Solution()
    prices = [7, 1, 5, 3, 6, 4]
    print("Max Profit:", sol.stockBuySell(prices))


# Optimal Solution
"""
Approach :
1. Initialize:
    min_price as infinity (∞) to keep track of the minimum stock price seen so far.
    max_profit as 0.
2.Traverse the array once.
3. For each stock price:
    If it is smaller than min_price, update min_price.
    Otherwise, calculate the profit by selling on the current day:
        profit = current_price - min_price
    Update max_profit if this profit is larger.
4. Return max_profit.

Time Complexity : O(n)
Space Complexity : O(1)
"""
class Solution:
    def stockBuySell(self, prices):
        min_price = float('inf')
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            else:
                max_profit = max(max_profit, price - min_price)
        return max_profit

if __name__ == "__main__":
    obj = Solution()
    prices = [7, 1, 5, 3, 6, 4]
    print(obj.stockBuySell(prices))

