class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counterS = {}
        counterT = {}
        if len(s) != len(t):
            return False
        for l in range(0,len(s)):
            counterS[s[l]] = 1 + counterS.get(s[l],0)
            counterT[t[l]] = 1 + counterT.get(t[l],0)
        for s in counterS:
            if counterS[s] != counterT.get(s, 0):
                return False
        return True
            
        