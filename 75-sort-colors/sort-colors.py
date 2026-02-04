class Solution:
    def sortColors(self, nums: List[int]) -> None:


        low=0
        mid=0
        high=len(nums)

        while mid<high:
            if nums[mid]==0:
                nums[low],nums[mid]=nums[mid],nums[low]
                low+=1
                mid+=1
            elif nums[mid]==1:
                mid+=1
            else:
                nums[mid],nums[high-1]=nums[high-1],nums[mid]
                high-=1
        return nums

        