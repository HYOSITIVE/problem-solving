class Solution:
    def isPalindrome(self, x: int) -> bool:
        reversed = str(x)[::-1]
        return str(x) == reversed