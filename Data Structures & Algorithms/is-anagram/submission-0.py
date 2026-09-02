class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}

        for word in s:
            if word in d: d[word] += 1
            else: d[word] = 1

        for word in t:
            if word not in d: return False
            else: 
                d[word] -= 1

        for word in d.keys():
            if d[word] != 0: return False

        return True