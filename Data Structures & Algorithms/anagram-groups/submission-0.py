from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # lst = []
        # skip_lst = []
        # for i in range(0,len(strs)):
        #     s = strs[i]
        #     flag = 0
        #     int_list = []
        #     if i in skip_lst:
        #         continue
        #     for j in range(i+1, len(strs)):
        #         count = {}
        #         t = strs[j]
        #         if len(s)!=len(t):
        #             continue
        #         for c in s:
        #             count[c] = count.get(c,0) +1
        #         for c in t:
        #             count[c] = count.get(c,0)-1
        #         if all(v==0 for v in count.values()):
        #             skip_lst.append(j)
        #             flag = 1
        #             int_list.append(s)
        #             int_list.append(t)
        #     if flag==0:
        #         lst.append([s])
        #     else:
        #         int_list  = set(int_list)
        #         lst.append(int_list)
        # return lst
        anagrams_dct = defaultdict(list)
        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c)-ord('a')] +=1
            key = tuple(count)
            anagrams_dct[key].append(s)
        return list(anagrams_dct.values())