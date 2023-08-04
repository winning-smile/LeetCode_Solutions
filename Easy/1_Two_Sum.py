"""
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""

class Solution:
    def __init__(self, nums, target):
        self.val = self.twoSum(nums, target)
    def twoSum(self, nums, target):
        array = nums.copy()
        for i in range(len(nums)-1):
            tmp = nums.pop()
            tmpi = array.index(tmp)
            for i in range(len(array)):
                if i!= tmpi and tmp + array[i] == target:
                    print([tmpi, i])
                    return True

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    answer = Solution(nums=[2,7,11,15], target=9)