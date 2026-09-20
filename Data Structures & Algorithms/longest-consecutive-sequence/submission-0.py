class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums = sorted(list(set(nums)))
        l = r = 0
        n = len(nums)
        longest = 0
        print(nums)
        while r < n:
            
            if r > 0 and nums[r] != nums[r - 1] + 1:
                l = r

            longest = max(longest, r-l + 1)
 

            r += 1
        
        return longest
