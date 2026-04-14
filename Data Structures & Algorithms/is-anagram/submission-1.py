class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        string1 = list(s)
        string2 = list(t)

        string1.sort()
        string2.sort()

        if string1 == string2:
            return True
        else:
            return False
