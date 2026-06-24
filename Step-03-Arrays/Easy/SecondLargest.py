"""
Problem :
Given an array of integers nums, return the second-largest element in the array. 
If the second-largest element does not exist, return -1.

Example 1 : Input: nums = [8, 8, 7, 6, 5]
            Output: 7
            Explanation : The largest value in nums is 8, the second largest is 7


Approach :
1. Sort the array in ascending order.
2. The largest element will be at index n - 1.
3. Traverse the sorted array from right to left.
4. Find the first element that is different from the largest element.
5. That element is the second largest.
6. Print the result.

Time Complexity : O(n log n)
Space Complexity : O(n)
"""
# Brute Force
class Solution:
    def secondLargestElement(self,arr,n):
        if n < 2:
            return -1
        arr.sort()
        smallest = arr[0]
        largest = arr[n-1]
        for i in range(n-2,0,-1):
            if arr[i] != largest:
                secondLargest = arr[i]
                break
        print(secondLargest)
        print(smallest)
        
if __name__ == "__main__":
    sol = Solution()
    arr = [24,1,4,12,5]
    n = len(arr)
    sol.secondLargestElement(arr,n)


# Better Solution
"""
Approach :
1. Find the largest element in the array.
2. Initialize secondLargest = -1.
3. Traverse the array again.
4. For every element:
    It should not be equal to the largest element.
    It should be greater than the current secondLargest.
5. Update secondLargest whenever a better candidate is found.
6. Print the second largest element.

Time Complexity : O(2N)
Space Complexity : O(1)
"""
class Solution:
    def secondLargestElement(self, arr, n):
        if n < 2:
            return -1
        largest = arr[0]
        for i in range(0,n):
            if arr[i] > largest:
                largest = arr[i]
        secondLargest = -1
        for i in range(0,n):
            if arr[i] > secondLargest and arr[i] != largest:
                secondLargest = arr[i]
        print(secondLargest)
        
if __name__ == "__main__":
    sol = Solution()
    arr = [24,1,4,12,5]
    n = len(arr)
    sol.secondLargestElement(arr,n)


# Optimal Solution
"""
Approach :
Finding Second Largest
    1.  Maintain two variables:
            largest
            secondLargest
    2.  Traverse the array once.
    3.  If a larger element is found:
            Update secondLargest = largest
            Update largest = current element
    4.  Otherwise, if the current element lies between largest and secondLargest, update secondLargest.

Finding Second Smallest
    1. Maintain:
        smallest
        sSmallest
    2. Traverse the array once.
    3. If a smaller element is found:
        Update sSmallest = smallest
        Update smallest = current element
    4. Otherwise, if the current element lies between smallest and sSmallest, update sSmallest.

Time Complexity : O(N)
Space Complexity : O(1)
"""
class Solution:
    def secondLargest(self,arr,n):
        largest = arr[0]
        secondLargest = -1
        for i in range(1,n):
            if arr[i] > largest:
                secondLargest = largest
                largest = arr[i]
            elif arr[i] < largest and arr[i] > secondLargest:
                secondLargest = arr[i]
        return secondLargest

    def secondSmallest(self,arr,n):
        smallest = arr[0]
        sSmallest = float('inf') 
        for i in range(1,n):
            if arr[i] < smallest:
                sSmallest = smallest
                smallest = arr[i]
            elif arr[i] != smallest and arr[i] < sSmallest:
                sSmallest = arr[i]
        return sSmallest

    def secondLargestElement(self,arr,n):
        sLargest = self.secondLargest(arr,n)
        sSmallest = self.secondSmallest(arr,n)
        return{sLargest,sSmallest}
        
if __name__ == "__main__":
    sol = Solution()
    arr = [24,1,4,12,5]
    n = len(arr)
    print(sol.secondLargestElement(arr,n))