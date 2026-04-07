class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p = list(p)
        n = len(p)
        s = list(s)
        p.sort()
        rt = []
        for i in range(len(s)-n+1):
            a = s[i:i+n]
            a.sort()
            if a == p:
                rt.append(i)
        return rt