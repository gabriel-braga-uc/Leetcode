class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        #sss
        while len(t) > 1:
            for x in s:
                for y in t:
                    if x == y:
                        t = t.replace(y, '', 1)
                        print(len(t))
                        break
                if len(t) == 1:
                    break
        return (t[0])