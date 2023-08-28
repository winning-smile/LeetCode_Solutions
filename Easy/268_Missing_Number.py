class Solution:
    """Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array."""
    def missingNumber(self, nums: List[int]) -> int:
        if len(nums)%2 == 0:
            half = len(nums)/2
        else:
            half = (len(nums)+1)/2

        flag = True

        if flag:
            for i in range(int(half)):
                if i in nums:
                    continue
                else:
                    return i

            flag = False

        if not flag:
            for i in range(int(half), len(nums)+1):
                if i in nums:
                    continue
                else:
                    return i
