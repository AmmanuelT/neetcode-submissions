from functools import reduce
class Solution:

    def encode(self, strs: List[str]) -> str:
        return reduce(lambda a, b: a + str(len(b)) + "#" + b, strs, "")
    def decode(self, s: str) -> List[str]:
        res = []
        while s:
            start = s.index("#") + 1
            length = int(s[:start - 1])
            res.append(s[start:start + length ])
            s = s[start + length:]
        return res
