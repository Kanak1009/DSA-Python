"""
Problem :
Print a given name N times using recursion.

Approach :
1. Create a recursive function printName(name, count, N).
2. Use a base case:
      - If count == N, stop the recursion and return.
3. Print the given name.
4. Recursively call the function with count + 1.
5. Repeat until the name has been printed N times.

Time Complexity : O(N)
Space Complexity : O(N)

"""

class Solution:
    def printName(self, name, count, N):
        if count == N:
            return
        print(name)

        self.printName(name, count + 1, N)

if __name__ == "__main__":
    sol = Solution()
    N = 5
    name = "Ashish"

    sol.printName(name, 0, N)
