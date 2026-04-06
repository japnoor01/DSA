class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        maxend=0
        minend=0
        maxsum=0
        minsum=0

        for i in range(len(nums)):
            maxend=max(maxend+nums[i],nums[i])
            minend=min(minend+nums[i],nums[i])

            maxsum=max(maxsum,maxend)
            minsum=min(minsum,minend)
        return max(maxsum,abs(minsum))
        