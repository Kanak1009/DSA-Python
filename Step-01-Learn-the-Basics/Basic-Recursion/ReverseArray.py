"""
Problem :
Given an array arr of n elements. The task is to reverse the given array. The reversal of array should be inplace.
Example 1 : Input: n=5, arr = [1,2,3,4,5]
            Output: [5,4,3,2,1]
            Explanation: The reverse of the array [1,2,3,4,5] is [5,4,3,2,1]


Approach :
1. Find the size of the array n.
2. Create a new array ans of size n.
3. Traverse the original array from left to right.
4. For each index i, place the element from the opposite end of the original array:
    ans[i] = arr[n - 1 - i]
5. Return the new reversed array.

Time Complexity : O(n)
Space Complexity : O(n)
"""
# Brute Force
class Solution:
    def reverseArray(self, arr):
        n = len(arr)
        ans = [0] * n
        for i in range(n):
            ans[i] = arr[n - 1 - i]
        return ans

if __name__ == "__main__":
    sol = Solution()
    arr = [1, 2, 3, 4, 5]
    result = sol.reverseArray(arr)
    print(result)


# Better Approach

"""
Approach :
1. Initialize two pointers:
        p1 = 0 (start of the array)
        p2 = len(arr) - 1 (end of the array)
2. While p1 < p2:
        Swap the elements at p1 and p2.
        Move p1 one step forward.
        Move p2 one step backward.
3. Continue until the pointers meet or cross.
4. The array gets reversed in-place.

Time Complexity : O(n)
Space Complexity : O(1)


"""
class Solution:
    def reverseArray(self, arr):
        p1 = 0
        p2 = len(arr) - 1
        while p1 < p2:
            arr[p1], arr[p2] = arr[p2],arr[p1]
            p1 +=1
            p2 -= 1
if __name__ == "__main__":
    sol = Solution()
    arr = [1, 2, 3, 4, 5]
    sol.reverseArray(arr)
    print(" ".join(map(str, arr)))




# Built-in Library Function Approach
"""
Approach :
1. Use Python slicing with a step of -1:
        arr[::-1]
2. This creates a new list containing the elements of arr in reverse order.
3. Assign the reversed list back to the original array using:
        arr[:] = arr[::-1]
4. The contents of arr are updated in-place from the caller's perspective.

Time Complexity : O(n)
Space Complexity : O(n)


"""
class Solution:
    def reverseArray(self, arr):
        arr[:] = arr[::-1]
if __name__ == "__main__":
    sol = Solution()
    arr = [1, 2, 3, 4, 5]
    sol.reverseArray(arr)
    print(" ".join(map(str, arr)))
