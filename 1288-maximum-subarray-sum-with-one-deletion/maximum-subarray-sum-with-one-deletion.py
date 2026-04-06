class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        
            no_del = arr[0]  # max sum without deletion
            one_del = 0  # max sum with one deletion
            ans = arr[0]

            for i in range(1, len(arr)):
                one_del = max(no_del, one_del + arr[i])
                no_del = max(arr[i], no_del + arr[i])
                ans = max(ans, no_del, one_del)

            return ans
