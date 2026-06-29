"""
Problem :
Given an integer array nums of size n, return the majority element of the array.
The majority element of an array is an element that appears more than n/2 times in the array. 
The array is guaranteed to have a majority element.

Example 1 : Input: nums = [7, 0, 0, 1, 7, 7, 2, 7, 7]
            Output: 7
            Explanation : The number 7 appears 5 times in the 9 sized array

Approach :
1. Traverse each element in the array.
2. For every element, count how many times it appears by scanning the entire array.
3. If its count is greater than n // 2, return that element.
4. Since the problem guarantees a majority element exists, the function will always return one.

Time Complexity : O(n²)
Space Complexity : O(1)
"""
# Brute Force
class Solution:
    def majorityElement(self,arr):
        n = len(arr)
        for i in range(n):
            cnt = 0
            for j in range(n):
                if arr[j] == arr[i] :
                    cnt += 1
            if cnt > (n // 2):
                return arr[i]

if __name__ == "__main__":
    arr = [2,2,3,3,1,2,2]
    sol = Solution()
    print(sol.majorityElement(arr))


# Better Approach
"""
Approach :
1. Create an empty dictionary mp.
2. Traverse the array and count the frequency of every element.
3. Traverse the dictionary.
4. If any element has a frequency greater than n // 2, return that element.
5. If no such element exists, return -1.

Time Complexity : O(n)
Space Complexity : O(n)
"""
class Solution:
    def majorityElement(self,arr):
        n = len(arr)
        mp = {}
        for num in arr:
            if num in mp:
                mp[num] += 1
            else:
                mp[num] = 1
        
        for num, count in mp.items():
            if count > n // 2:
                return num
        return -1

if __name__ == "__main__":
    arr = [2,2,3,3,1,2,2]
    sol = Solution()
    print(sol.majorityElement(arr))



# Optimal Solution
"""
Approach :
The algorithm works in two phases.

Phase 1: Find the Candidate
1. Initialize:
    cnt = 0
    el = 0
2. Traverse the array:
    If cnt == 0, make the current element the new candidate.
    If the current element equals the candidate, increment cnt.
    Otherwise, decrement cnt.
3. At the end of the traversal, el is the potential majority element.

Phase 2: Verify the Candidate
1. Count the occurrences of el.
2. If its frequency is greater than n // 2, return it.
3. Otherwise, return -1

Time Complexity : O(n)
Space Complexity : O(1)
"""
class Solution:
    def majorityElement(self,arr):
        n = len(arr)
        cnt = 0
        cnt1 = 0
        el = 0
        for i in range(n):
            if cnt == 0:
                cnt = 1
                el = arr[i]
            elif arr[i] == el:
                cnt += 1
            else:
                cnt -= 1
        for i in range(n):
            if arr[i] == el:
                cnt1 += 1
        if cnt1 > (n // 2):
            return el
        return -1

if __name__ == "__main__":
    arr = [2,2,3,3,1,2,2]
    sol = Solution()
    print(sol.majorityElement(arr))
