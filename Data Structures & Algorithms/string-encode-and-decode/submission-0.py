class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += str(len(s)) + "#" + s

        return result   

    def decode(self, s: str) -> List[str]:
        result = []
        stringIndex = 0

        while stringIndex < len(s):
            delimiterFinder = stringIndex
            while s[delimiterFinder] != "#":
                delimiterFinder += 1

            length = int(s[stringIndex:delimiterFinder])

            result.append(s[delimiterFinder + 1 : delimiterFinder + 1 + length])
            stringIndex = delimiterFinder + 1 + length
        
        return result
            
