class Solution:
    def minSubArrayLen(self, target: int, arr: List[int]) -> int:
        
        n=len(arr)
        low=0
        high=0
        sum=0
        window_size=float('inf')

        while high<n:
            sum=sum+arr[high]

            while sum>=target:
                length=high-low+1
                window_size=min(window_size,length)
                sum=sum-arr[low]
                low+=1
                
            high+=1
            
        return window_size if window_size !=float('inf') else 0
    
        