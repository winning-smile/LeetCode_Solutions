class Solution:
    """An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.
    Given an integer n, return true if n is an ugly number."""
    def isUgly(self, n: int) -> bool:
        flag = True
        while flag:
            if n:
                if n % 2 == 0:
                    n = n // 2
                elif n % 3 == 0:
                    n = n // 3
                elif n % 5 == 0:
                    n = n // 5
                elif n == 1:
                    return True
                else:
                    return False
            else:
                return False