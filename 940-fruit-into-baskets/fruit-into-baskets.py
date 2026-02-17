class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n=len(fruits)
        low=0
        high=0
        f={}
        res=0

        for i in range(n):
            f[fruits[i]]=f.get(fruits[i],0)+1

            while len(f)>2:
                f[fruits[low]]-=1
                if f[fruits[low]]==0:
                    del f[fruits[low]]
                low +=1

            
            res= max(res,i-low+1)
        
        return res