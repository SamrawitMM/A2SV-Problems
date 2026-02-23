class Solution:
    def isPalindrome(self, s: str) -> bool:
        reversed_s = s.lower().strip()
        reversed_s = [char for char in reversed_s if char.isalnum()]
        if "".join(reversed_s[::-1]) == "".join(reversed_s):
            return True
        else:
            return False
        
