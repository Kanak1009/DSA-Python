"""
Problem :
Given two sorted arrays nums1 and nums2, return an array that contains the intersect of these two arrays. 
The elements in the intersect must be in ascending order.
The intersect of two arrays is an array where all values are distinct and are present in either the first array, the second array, 
or both.

Example 1 : Input: nums1 = [1, 2, 3, 4, 5], nums2 = [1, 2, 7]
            Output: [1, 2]
            Explanation : The elements 1, 2 are common to both nums1 and num2


Approach :
1. Initialize two pointers:
    i for arr1
    j for arr2
2. Compare the current elements:
    If arr1[i] < arr2[j], move i forward.
    If arr2[j] < arr1[i], move j forward.
    If both are equal, add the element to the intersection array and move both pointers.
3. Continue until one of the arrays is completely traversed.
4. Return the intersection array.

Time Complexity : O(n + m)
Space Complexity : O(k) (O(1) auxiliary space excluding the output array)
"""
class Solution:
    def intersectArray(self, arr1, arr2,n,m):
        i,j =0,0
        ans =[]
        while(i<n and j < m):
            if (arr1[i]< arr2[j]):
                i += 1
            elif (arr2[j] < arr1[i]):
                j += 1
            else:
                ans.append(arr1[i])
                i += 1
                j += 1
        return ans


if __name__ == "__main__":
    arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    arr2 = [2, 3, 4, 4, 5, 11, 12]
    n = len(arr1)
    m = len(arr2)
    obj = Solution()
    result = obj.intersectArray(arr1, arr2,n,m)
    print("Intersect of arr1 and arr2 is:", *result)