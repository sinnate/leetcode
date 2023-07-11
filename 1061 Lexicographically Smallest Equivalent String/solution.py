class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        n = list(range(26))
        def find(x):
            if n[x] != x:
                n[x] = find(n[x])
            return n[x]
        for i in range(len(s1)):
            a, b = ord(s1[i]) - ord('a'), ord(s2[i]) - ord('a')
            na, nb = find(a), find(b)
            if na < nb:
                n[nb] = na
            else:
                n[na] = nb

        res = []
        for a in baseStr:
            a = ord(a) - ord('a')
            res.append(chr(find(a) + ord('a')))
        return ''.join(res)