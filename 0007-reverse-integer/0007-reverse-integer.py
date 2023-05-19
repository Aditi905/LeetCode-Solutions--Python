class Solution:
    def reverse(self, x: int) -> int:
        rev_x = 0
        neg = x < 0
        x = abs(x)
        while x != 0:
            pop = x % 10
            x //= 10
            rev_x = rev_x * 10 + pop

        if neg:
            rev_x *= -1
        if rev_x < -2**31 or rev_x > 2**31 - 1:
            return 0
        else:
            return rev_x

        
        