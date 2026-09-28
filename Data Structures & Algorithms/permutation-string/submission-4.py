class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        counts = [0] * 26
        for char in s1:
            counts[ord(char) - ord('a')] += 1
        print(counts)
        l = r = 0

        while r < len(s2):
            current = s2[r]
            counts[ord(current) - ord('a')] -= 1
            r+= 1

            while counts[ord(current) - ord('a')] < 0:
                l_current = s2[l]
                counts[ord(l_current) - ord('a')] += 1
                l+= 1

            if sum(counts) == 0:
                return True

        return False
            