""" just programm fibbonaci"""
class Solution:
    def climbStairs(self, n: int) -> int:
        constanst = [1, 2]
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            for i in range(2, n):
                constanst.append(constanst[-1] + constanst[-2])
            return constanst[n-1]