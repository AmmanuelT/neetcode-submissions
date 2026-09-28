class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        # binary search 
        # if sorted return first
        # Else break into two search in unsorted
         
        n = len(nums)
        l = 0
        r = n - 1

        while l < r:
            #print(f'l: {l}, r:{r}')
            # opt 1 already sorted
            if nums[l] < nums[r]:
                return nums[l]

            # at the item
            if l == r:
                return nums[l]
            
            middle = (l + r) // 2
            # left is unsorted
            if nums[l] > nums[middle]:
                r = middle
            # right is unsorted
            elif nums[middle] > nums[r]:
                l = middle + 1

            
        
        return nums[l]
            