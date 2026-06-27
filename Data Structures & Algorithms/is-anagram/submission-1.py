class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        dct = {}
        for c in s:
            dct[c] = dct.get(c,0)+1
        for c in t:
            dct[c] = dct.get(c,0)-1
        return all(v==0 for v in dct.values())
        