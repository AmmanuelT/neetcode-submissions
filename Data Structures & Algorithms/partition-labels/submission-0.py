class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hashmap = {char: s.rfind(char) for char in set(s)}

        start = end = 0
        res = []
        for index, char in enumerate(s):
            
            if index > end:
                res.append(end-start+1)
                start = end = index
                


            end = max(end, hashmap[char])

            if index == len(s) - 1:
                res.append(end-start+1)
        
        return res
