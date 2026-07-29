class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dct = {}
        for c in s:
            dct[c] = dct.get(c,0)+1
        for c in t:
            dct[c] = dct.get(c,0)-1
        for k,v in dct.items():
            if v!=0:
                return False
        return True


        