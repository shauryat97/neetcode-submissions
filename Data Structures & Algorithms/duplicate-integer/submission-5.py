class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dct = {}
        for ele in nums:
            dct[ele] = dct.get(ele,0)+1
        for k,v in dct.items():
            if v>=2:
                return True
        return False