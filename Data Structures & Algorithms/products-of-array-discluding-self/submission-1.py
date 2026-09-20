class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix  = [0] * n
        postfix  = [0] * n

        prefix[1] = nums[0]
        postfix[-2] = nums[-1]
        for i in range(2,n):          
            prefix[i] = prefix[i-1] * nums [i-1]
            postfix[(n-1) - i] = postfix[(n-1) - i + 1] * nums[(n-1) - i + 1]

        nums[0] = postfix[0]
        nums[-1] = prefix[-1]

        for i in range(1,n-1):
            nums[i] = prefix[i] * postfix[i]
        
        return nums