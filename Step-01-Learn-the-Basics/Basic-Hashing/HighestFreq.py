"""
Problem : 
Given an array nums of n integers, find the most frequent element in it i.e., the element that occurs the maximum number of times. 
If there are multiple elements that appear a maximum number of times, find the smallest of them.
Example 1 : Input: nums = [1, 2, 2, 3, 3, 3]
            Output: 3
            Explanation: The number 3 appears the most (3 times). It is the most frequent element.


Approach : 
1. Create a visited array to keep track of elements whose frequencies have already been counted.
2. Traverse the array.
3. For each unvisited element:
    Count its occurrences by scanning the remaining part of the array.
    Mark duplicate occurrences as visited.
4. Compare the frequency (count) with:
    maxFreq → update the highest frequency element.
    minFreq → update the lowest frequency element.
5. After processing all elements, print:
    Element with maximum frequency.
    Element with minimum frequency.

Time Complexity : O(n²)
Space Complexity : O(n)
"""

# Brute Force
class FrequencyCounter:
    def countFreq(self, arr):
        n = len(arr)                     
        visited = [False] * n           
        maxFreq = 0                     
        minFreq = n                     
        maxEle = 0                      
        minEle = 0                      

        for i in range(n):
            if visited[i]:
                continue

            count = 1
            for j in range(i + 1, n):
                if arr[i] == arr[j]:
                    visited[j] = True   
                    count += 1

            if count > maxFreq:
                maxEle = arr[i]
                maxFreq = count

            if count < minFreq:
                minEle = arr[i]
                minFreq = count

        print("The highest frequency element is:", maxEle)
        print("The lowest frequency element is:", minEle)


if __name__ == "__main__":
    fc = FrequencyCounter()         
    arr = [10, 5, 10, 15, 10, 5]                
    fc.countFreq(arr)                           




# Optimal Approach
"""
Approach : 
1. Create a dictionary (freq_map) to store the frequency of each element.
2. Traverse the array and update the frequency count:
    freq_map[num] = freq_map.get(num, 0) + 1
3. Initialize:
    maxFreq = 0
    minFreq = len(arr)
4. Traverse the frequency map:
    If the current frequency is greater than maxFreq, update the highest frequency element.
    If the current frequency is less than minFreq, update the lowest frequency element.
5. Print the elements having the highest and lowest frequencies.

Time Complexity : O(n)
Space Complexity : O(n)

"""
class FrequencyCounter:
    def Frequency(self, arr):
        freq_map = {} 
        for num in arr:
            freq_map[num] = freq_map.get(num, 0) + 1

        maxFreq = 0
        minFreq = len(arr)
        maxEle = 0
        minEle = 0

        for element, count in freq_map.items():
            if count > maxFreq:
                maxFreq = count
                maxEle = element

            if count < minFreq:
                minFreq = count
                minEle = element

        print("The highest frequency element is:", maxEle)
        print("The lowest frequency element is:", minEle)


if __name__ == "__main__":
    fc = FrequencyCounter()
    arr = [10, 5, 10, 15, 10, 5]
    fc.Frequency(arr)
