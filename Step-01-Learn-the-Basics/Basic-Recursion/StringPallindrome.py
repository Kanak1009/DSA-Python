"""
Problem :
Given a string s, return true if the string is palindrome, otherwise false.
A string is called palindrome if it reads the same forward and backward.
Example 1 : Input : s = "hannah"
            Output : true
            Explanation : The string when reversed is --> "hannah", which is same as original string , so we return true.


Approach :
1. Initialize two pointers:
        left = 0 (start of the string)
        right = len(s) - 1 (end of the string)
2. While left < right:
        If s[left] is not alphanumeric, move left forward.
        If s[right] is not alphanumeric, move right backward.
        Compare characters after converting them to lowercase.
        If they are different, return False.
        Otherwise, move both pointers toward the center.
3. If all character pairs match, return True.
This approach handles:
        Uppercase/lowercase differences
        Spaces
        Special characters

Time Complexity : O(n)
Space Complexity : O(1)
"""
# Brute Force Approach
class Solution:
    def palindromeCheck(self, s):
        left, right = 0, len(s) - 1
        while left < right:
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            elif s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1
        return True
if __name__ == "__main__":
    sol = Solution()
    s = "adbada"
    ans = sol.palindromeCheck(s)
    if ans:
        print("Palindrome")
    else:
        print("Not Palindrome")


# Optimal Approach (Recursion)
""" 
Approach :
1. Start comparing characters from both ends of the string.
2. At each recursive call:
    Compare s[i] with s[len(s) - i - 1].
3. If the characters do not match, return False.
4. If i reaches the middle of the string, all characters have matched, so return True.
5. Otherwise, recursively check the next pair by calling:
    self.palindromeCheck(i + 1, s)


Time Complexity : O(n)
Space Complexity : O(n)

"""
class Solution:
    def palindromeCheck(self,i,s):
        if i >= len(s) // 2:
            return True
        if s[i] != s[len(s) - i - 1]:
            return False
        return self.palindromeCheck(i + 1, s)

if __name__ == "__main__":
    sol = Solution()
    s = "kanak"
    ans = sol.palindromeCheck(0,s)
    if ans:
        print("Palindrome")
    else:
        print("Not Palindrome")