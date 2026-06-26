"""
Problem :
Given two sorted arrays nums1 and nums2, return an array that contains the union of these two arrays. 
The elements in the union must be in ascending order.
The union of two arrays is an array where all values are distinct and are present in either the first array, the second array, 
or both.

Example 1 : Input: nums1 = [1, 2, 3, 4, 5], nums2 = [1, 2, 7]
            Output: [1, 2, 3, 4, 5, 7]
            Explanation : The elements 1, 2 are common to both, 3, 4, 5 are from nums1 and 7 is from nums2


Approach :
1. Create an empty dictionary freq.
2. Traverse the first array and insert each element into the dictionary.
3. Traverse the second array and insert each element into the same dictionary.
4. Since dictionary keys are unique, duplicate elements are stored only once.
5. Extract all keys from the dictionary and sort them.
6. Return the sorted list of unique elements as the union.

Time Complexity :
O(n + m + k log k), where k is the number of unique elements.
Worst Case: O((n + m) log(n + m))
Space Complexity : O(n + m)
"""
# Approach 1 : Using Map
class Solution:
    def FindUnion(self, arr1, arr2, n, m):
        freq = {}
        for i in range(n):
            freq[arr1[i]] = freq.get(arr1[i], 0) + 1
        for i in range(m):
            freq[arr2[i]] = freq.get(arr2[i], 0) + 1
        Union = sorted(freq.keys())
        return Union

if __name__ == "__main__":
    n = 10
    m = 7
    arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    arr2 = [2, 3, 4, 4, 5, 11, 12]
    obj = Solution()
    Union = obj.FindUnion(arr1, arr2, n, m)
    print("Union of arr1 and arr2 is :")
    print(Union)


# Approach 2 : Using Set
"""
Approach :
1. Convert both arrays into sets.
2. A set automatically removes duplicate elements.
3. Compute the union of the two sets using the | operator.
4. Sort the resulting set to return the elements in ascending order.
5. Return the sorted union.

Time Complexity :
O(n + m + k log k)
Worst Case: O((n + m) log(n + m))
Space Complexity : O(n + m)
"""
class Solution:
    def findUnion(self, arr1, arr2):
        st = set(arr1) | set(arr2)
        return sorted(st)

if __name__ == "__main__":
    arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    arr2 = [2, 3, 4, 4, 5, 11, 12]
    obj = Solution()
    result = obj.findUnion(arr1, arr2)
    print("Union of arr1 and arr2 is:", *result)


# Optimal Solution
"""
Approach :
1. Initialize two pointers:
    i for arr1
    j for arr2
2. Compare the current elements of both arrays:
    If arr1[i] <= arr2[j], process arr1[i] and move i.
    Otherwise, process arr2[j] and move j.
3. Before adding an element to the union array, check whether it is already the last inserted element to avoid duplicates.
4. After one array is completely traversed, add the remaining elements of the other array while avoiding duplicates.
5. Return the union array.

Time Complexity : O(n + m)
Space Complexity : O(n + m)
                   (O(1) auxiliary space excluding the output array)
"""
class Solution:
    def findUnion(self, arr1, arr2):
        n1 = len(arr1)
        n2 = len(arr2)

        i, j = 0, 0
        unionArr = []

        while i < n1 and j < n2:
            if arr1[i] <= arr2[j]:
                if len(unionArr) == 0 or unionArr[-1] != arr1[i]:
                    unionArr.append(arr1[i])
                i += 1
            else:
                if len(unionArr) == 0 or unionArr[-1] != arr2[j]:
                    unionArr.append(arr2[j])
                j += 1

        while i < n1:
            if len(unionArr) == 0 or unionArr[-1] != arr1[i]:
                unionArr.append(arr1[i])
            i += 1

        while j < n2:
            if len(unionArr) == 0 or unionArr[-1] != arr2[j]:
                unionArr.append(arr2[j])
            j += 1

        return unionArr


if __name__ == "__main__":
    arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    arr2 = [2, 3, 4, 4, 5, 11, 12]

    obj = Solution()
    result = obj.findUnion(arr1, arr2)
    print("Union of arr1 and arr2 is:", *result)
