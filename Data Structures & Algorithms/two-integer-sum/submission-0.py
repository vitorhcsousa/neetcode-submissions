class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            num_0 = nums[i]
            for l in range(0, len(nums)):
                num_1 = nums[l]
                if (i!=l) & ((num_0+num_1) == target):
                    return [i,l]
        