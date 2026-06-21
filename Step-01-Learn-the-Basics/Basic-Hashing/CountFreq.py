"""
Problem : 
Given an array nums of size n which may contain duplicate elements.
Return a list of pairs where each pair contains a unique element from the array and its frequency in the array.
You may return the result in any order, but each element must appear exactly once in the output.
Example 1 : Input: nums = [1, 2, 2, 1, 3]
            Output: [[1, 2], [2, 2], [3, 1]]
            Explanation: - 1 appears 2 times
                         - 2 appears 2 times
                         - 3 appears 1 time
            Order of output can vary.


Approach : 
1. Create a visited array of size n initialized with False.
2. Traverse the array using index i.
3. If the current element has already been counted (visited[i] == True), skip it.
4. Otherwise:
    Initialize count = 1.
    Traverse the remaining elements (j = i+1 to n-1).
    If the same element is found, mark it as visited and increment the count.
5. After counting all occurrences, print the element and its frequency.

Time Complexity : O(n²)
Space Complexity : O(n)
"""

# Brute Force
class Solution:
    def countFrequencies(self, nums):
        n = len(nums)
        visited = [False] * n
        for i in range(n):
            if visited[i]:
                continue

            count = 1

            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    visited[j] = True
                    count += 1

            print(nums[i], count)


if __name__ == "__main__":
    sol = Solution()
    arr = [10, 5, 10, 15, 10, 5]

    sol.countFrequencies(arr)


# Optimal Approach
"""
Approach : 
1. Create a defaultdict(int) to store frequencies.
2. Every new key automatically gets a default value of 0.
3. Traverse the array once.
4. For each element, increment its count in the dictionary:
    freq_map[arr[i]] += 1
5. After counting all elements, traverse the dictionary and print each element along with its frequency.

Time Complexity : O(n)
Space Complexity : O(n)

"""
from collections import defaultdict
class Solution:
    def Frequency(self, arr, n):
        freq_map = defaultdict(int)

        for i in range(n):
            freq_map[arr[i]] += 1

        for key, value in freq_map.items():
            print(key, value)

if __name__ == "__main__":
    arr = [10, 5, 10, 15, 10, 5]
    n = len(arr)

    sol = Solution()

    sol.Frequency(arr, n)
