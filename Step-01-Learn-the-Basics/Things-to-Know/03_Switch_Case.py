"""
Problem: Given the integer day denoting the day number, print on the screen which day of the week it is. 
         Week starts from Monday and for values greater than 7 or less than 1, print Invalid.
         Ensure only the 1st letter of the answer is capitalised.


Approach: Match Case 

Time Complexity: O(1)
Space Complexity: O(1)
"""

class Solution:
    def whichweekDay(self,day):
        match day:
            case 1:
                return "Monday"
            case 2:
                return "Tuesday"
            case 3:
                return "Wednesday"
            case 4:
                return "Thursday"
            case 5:
                return "Friday"
            case 6:
                return "Saturday"
            case 7:
                return "Sunday"
            case _:
                return "Invalid"
if __name__ == "__main__":
    sol = Solution()
    week = sol.whichweekDay(3)
    print(week)