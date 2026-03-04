class Solution:
    def isHappy(self, n: int) -> bool:
         def fun(n):
            sum =0
            while(n>0):
                d=n%10
                n=n//10
                sum =sum +d*d
            return sum
         slow =n
         fast=n
         while True:
            slow=fun(slow)
            fast=fun(fun(fast))
            if fast==1 or slow==1:
                return True
            
            if fast==slow:
                return False
            if fast==1:
                return True
                


        