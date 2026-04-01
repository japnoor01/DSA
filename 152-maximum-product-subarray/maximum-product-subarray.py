class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        minend = nums[0]
        maxend = nums[0]
        ans = nums[0]

        for i in range(1, len(nums)):
            v1 = maxend * nums[i]
            v2 = minend * nums[i]
            v3 = nums[i]

            maxend = max(v1, v2, v3)
            minend = min(v1, v2, v3)

            ans = max(ans, maxend)

        return ans
        
        