"""
Problem: Input Output

Example 1 : Input(user gives value): 7
            Output: 7
Example 2 : Input(user gives value): -5
            Output: -5

Approach: 1. Read an integer from user
          2. Store it in variable called number
          3. Print the value of number

Time Complexity: O(1)
Space Complexity: O(1)
"""

def solve():
    number = int(input("Enter a number to print : "))
    print(number)

if __name__ == "__main__":
    solve()