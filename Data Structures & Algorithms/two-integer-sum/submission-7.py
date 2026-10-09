class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(0,len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i]+nums[j]==target:
        #             return [min(i,j), max(i,j)]


        for i in range(0, len(nums)-1):
            curr = nums[i]
            diff = target - curr
            for j in range(i+1, len(nums)):
                if nums[j]== diff:
                    return ([min(i,j), max(i,j)])
        

        