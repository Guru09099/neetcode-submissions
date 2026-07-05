class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sd = {}
        td = {}
        for i in s:
            if i not in sd:
                sd[i] = 1
            else:
                sd[i] += 1
        for i in t:
            if i not in td:
                td[i] = 1
            else:
                td[i] += 1
        return sd == td