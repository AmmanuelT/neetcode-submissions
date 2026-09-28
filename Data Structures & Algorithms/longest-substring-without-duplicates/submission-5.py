class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        state = defaultdict(int)

        l = r = 0
        longest = 0
        while r < len(s):
            current = str(s[r])
            state[current] += 1
            r+= 1

            while state[current] > 1:
                l_current = str(s[l])
                state[l_current] -= 1
                l += 1
            
            longest = max(longest, r - l)
        return longest
            
