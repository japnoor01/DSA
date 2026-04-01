class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
      
        minend=0
        maxend=0
        ans=float('-inf')
        for i in range(len(nums)):
            v1=maxend+nums[i]
            v2=minend+nums[i]
            v3=nums[i]
            maxend=max(v3,max(v1,v2))
            minend=max(v3,max(v1,v2))
            ans=max(ans,max(maxend,minend))        
        return ans
        