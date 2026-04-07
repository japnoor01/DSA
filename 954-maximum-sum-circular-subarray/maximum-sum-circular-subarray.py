class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
            maxend = minend = nums[0]
            maxsum = minsum = nums[0]
            total = nums[0]

            for i in range(1, len(nums)):
                x = nums[i]

                maxend = max(x, maxend + x)
                maxsum = max(maxsum, maxend)

                minend = min(x, minend + x)
                minsum = min(minsum, minend)

                total += x

            if maxsum < 0:
                return maxsum

            return max(maxsum, total - minsum)
        