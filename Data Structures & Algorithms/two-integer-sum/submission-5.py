class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for k in range(len(nums)):
            for i in range(len(nums)):
                if nums[k] + nums[i] == target and k != i:
                    return [k,i]
                