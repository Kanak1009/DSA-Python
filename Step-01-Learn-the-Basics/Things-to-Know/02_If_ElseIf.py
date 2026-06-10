"""
Problem: If-Else-If
        Given marks of a student, print on the screen:
            Grade A if marks >= 90
            Grade B if marks >= 70
            Grade C if marks >= 50
            Grade D if marks >= 35
            Fail, otherwise.

Example 1 : Input: marks = 95
            Output: Grade A
            Explanation: marks are greater than or equal to 90.

Example 2 : Input: marks = 14
            Output: Fail
            Explanation: marks are less than 35.

Approach:  Use an if-elif-else ladder.

Time Complexity: O(1)
Space Complexity: O(1)

"""

class Solution:
    def studentGrade(self,marks):
        if marks >= 90:
            return "Grade A"
        elif marks >= 70:
            return "Grade B"
        elif marks >= 50:
            return "Grade C"
        elif marks >= 35:
            return "Grade D"
        else:
            return "Fail"

if __name__ == "__main__":
    sol = Solution()
    grade = sol.studentGrade(95)
    # grade = sol.studentGrade(14)
    print(grade)