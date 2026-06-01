class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ''
        for letter in s:
            if letter.isalnum():
                newStr += letter.lower()
            
        return newStr == newStr[::-1]