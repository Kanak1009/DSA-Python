"""
Problem :
Given an integer array nums of even length consisting of an equal number of positive and negative integers.
Return the answer array in such a way that the given conditions are met:
    Every consecutive pair of integers have opposite signs.
    For all integers with the same sign, the order in which they were present in nums is preserved.
    The rearranged array begins with a positive integer.

Example 1 : Input : nums = [2, 4, 5, -1, -3, -4]
            Output : [2, -1, 4, -3, 5, -4]
            Explanation : The positive number 2, 4, 5 maintain their relative positions and -1, -3, -4 maintain their relative positions

Approach :
1. Create two separate lists:
    pos to store positive numbers.
    neg to store negative numbers.
2. Traverse the array once and place each element into its respective list.
3. Traverse the array again:
    Place positive numbers at even indices (0, 2, 4, ...).
    Place negative numbers at odd indices (1, 3, 5, ...).
4. Return the rearranged array.

Time Complexity : O(n)
Space Complexity : O(n)
"""
# Brute Force
class Solution:
    def reArrangeArray(self,arr):
        pos = []
        neg = []
        n = len(arr)
        for i in range(n):
            if arr[i] > 0:
                pos.append(arr[i])
            else:
                neg.append(arr[i])

        for i in range(0,n//2):
            arr[2*i] = pos[i]
            arr[2*i+1] = neg[i]
        return arr
if __name__ == "__main__":
    obj = Solution()
    arr = [3,1,-2,-5,2,-4]
    print(obj.reArrangeArray(arr))


# Optimal Solution
"""
Approach :
1. Create an answer array ans of size n.
2.Maintain two indices:
    pos = 0 → next even index for positive numbers.
    neg = 1 → next odd index for negative numbers.
3. Traverse the original array once.
4. If the current element is:
    Positive → place it at ans[pos] and increment pos by 2.
    Negative → place it at ans[neg] and increment neg by 2.
5.Return the rearranged array.

Time Complexity : O(n)
Space Complexity : O(n)
"""
class Solution:
    def reArrangeArray(self,arr):
        n = len(arr)
        ans = [0] * n
        pos = 0
        neg = 1
        for i in range(n):
            if arr[i] < 0:
                ans[neg] = arr[i]
                neg += 2
            else:
                ans[pos] = arr[i]
                pos += 2
        return ans
if __name__ == "__main__":
    obj = Solution()
    arr = [3,1,-2,-5,2,-4]
    print(obj.reArrangeArray(arr))
