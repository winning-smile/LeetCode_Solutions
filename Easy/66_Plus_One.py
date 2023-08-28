class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = list(reversed(digits))
        number = 0
        result = []
        for i in range(len(digits)):
            number += digits[i] * 10 ** i
        number += 1

        for num in str(number):
            result.append(int(num))

        return result

