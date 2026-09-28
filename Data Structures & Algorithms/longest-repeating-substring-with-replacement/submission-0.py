class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        counts = [0] * 26
        l = r = 0 

        longest = 0
        max_count = 0

        while r < len(s):
            current = s[r]
            counts[ord(current) - ord('A')] += 1
            max_count = max(max_count, counts[ord(current) - ord('A')])
            r += 1
            while r - l - max_count > k:
                l_current = s[l]
                counts[ord(l_current) - ord('A')] -= 1
                max_count = max(counts)
                l += 1
            
            longest = max(longest, r - l)
        print(counts)
        return longest