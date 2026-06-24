"""
Problem :
Given an integer array nums sorted in non-decreasing order, remove all duplicates in-place so that each unique element 
appears only once. Return the number of unique elements in the array.

If the number of unique elements be k, then,
Change the array nums such that the first k elements of nums contain the unique values in the order that they were present originally.
The remaining elements, as well as the size of the array does not matter in terms of correctness.
The driver code will assess correctness by printing and checking only the first k elements of the modified array.
An array sorted in non-decreasing order is an array where every element to the right of an element is either equal 
to or greater in value than that element.

Example 1 : Input: nums = [0, 0, 3, 3, 5, 6]
            Output: 4
            Explanation : Resulting array = [0, 3, 5, 6, _, _]
There are 4 distinct elements in nums and the elements marked as _ can have any value.


Approach :
1. Create a set called seen to keep track of unique elements.
2. Maintain an index pointer where the next unique element should be placed.
3. Traverse the array:
    If the element is not in seen:
        Add it to seen.
        Place it at nums[index].
        Increment index.
4. After the traversal, the first index positions of the array contain all unique elements.
5. Return index (the number of unique elements).


Time Complexity : O(n)
Space Complexity : O(n)
"""
# Brute Force
class Solution:
    def removeDuplicates(self, nums):
        seen = set()
        index = 0
        for num in nums:
            if num not in seen:
                seen.add(num)
                nums[index] = num
                index += 1
        return index
if __name__ == "__main__":
    nums = [24,1,4,12,5,12,24]
    sol = Solution()
    k = sol.removeDuplicates(nums)
    print("k =", k)
    print(nums[:k])

# Optimal Solution
"""
Approach :
This is the optimal two-pointer solution for removing duplicates from a sorted array.

1. Use two pointers:
    i → points to the last unique element.
    j → scans the array.
2. Start with:
    i = 0
    j = 1
3. Whenever nums[j] is different from nums[i]:
    Move i one step ahead.
    Place the new unique element at nums[i].
4. After the traversal:
    The first i + 1 elements contain all unique values.
5. Return i + 1 as the count of unique elements.

Time Complexity : O(n)
Space Complexity : O(1)
"""
class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        i = 0
        for j in range(1,len(nums)):
            if nums[j] != nums[i]:
                nums[i+1] = nums[j]
                i += 1
        return i + 1
if __name__ == "__main__":
    nums = [1,1,2,2,2,3,3]
    sol = Solution()
    k = sol.removeDuplicates(nums)
    print("k =", k)
    print(nums[:k])