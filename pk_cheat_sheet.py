class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = orig
        rev = 0
        while num > 0:
            rem = num % 10
            rev = (rev * 10) + rem
            num = num // 10
        return True