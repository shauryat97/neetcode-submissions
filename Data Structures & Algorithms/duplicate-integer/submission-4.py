class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dct = {}
        flag = 0
        for ele in nums:
            if dct.get(ele):
                flag=1
            else:
                dct[ele]=1
        if flag:
            return True
        return False
                
        # for i in range(0,len(nums)-1):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]==nums[j]:
        #             return True
        # return False