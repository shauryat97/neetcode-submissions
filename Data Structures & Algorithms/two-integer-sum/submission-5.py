class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # arr = [(num, i) for i,num in enumerate(nums)]
        # arr.sort()
        # l = 0
        # r = len(arr)-1
        # while l<=r:
        #     total = arr[l][0]+arr[r][0]
        #     if total==target:
        #         i = arr[l][1]
        #         j = arr[r][1]
        #         return [min(i,j), max(i,j)]
        #     elif arr[l][0]+arr[r][0]>target:
        #         r-=1
        #     else:
        #         l+=1
        dct = {}
        for i, num in enumerate(nums):
            diff = target-num
            if diff in dct:
                return [dct[diff],i]
            dct[num] = i