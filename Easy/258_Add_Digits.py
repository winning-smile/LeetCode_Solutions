class Solution:
    def addDigits(self, num: int) -> int:
        """Given an integer num, repeatedly add all its digits until the result has only one digit, and return it."""

        if num // 10 == 0:
            return num

        while True:
            remains = []
            c = 0
            while num:
                remains.append(num % 10)
                num = num // 10

            for elem in remains:
                c += elem

            if c // 10 == 0:
                return c
            else:
                num = c