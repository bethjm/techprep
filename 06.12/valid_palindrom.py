#I was really excited that I knew how to do this one!! (didnt know the syntax in python, but I knew what methods to use)

#question:
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.

#video to reference:
#https://www.youtube.com/watch?v=jJXJ16kPFWg

class Solution:
    def isPalidrome(self, s: str) -> bool:
        newStr = ""

        for c in s:
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1]
