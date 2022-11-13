class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashs = {}
        hasht = {}
        for w in s:
            hashs.setdefault(w, 0)
            hashs[w] += hashs[w] + 1
        for l in t:
            hasht.setdefault(l, 0)
            hasht[l] += hasht[l] + 1
        if hasht == hashs:
            return True
        else: 
            return False

    def faster(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        for idx in set(s):
            if s.count(idx) != t.count(idx):
                return False
        return False