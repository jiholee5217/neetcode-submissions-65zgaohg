class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += str(len(word)) + '#' + word
        return res

    def decode(self, s: str) -> List[str]:
        if not s:
            return []

        res = []

        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1: j + 1 + length])
            i = j + 1 + length
            j = i

        return res
'''     
52#

5#Hello6#World
01234567890123
i
 j

5#Hello6#World
0123455


Hello World
'''