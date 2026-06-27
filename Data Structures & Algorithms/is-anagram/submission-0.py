class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dct1 = {}
        dct2 = {}
        for c in s:
            dct1[c] = dct1.get(c,0)+1
        for c in t:
            dct2[c] = dct2.get(c,0) +1
        if dct1==dct2:
            return True
        else:
            return False
        