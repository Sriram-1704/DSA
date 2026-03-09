class Solution:
    def add_fraction(self,a,b,c,d):
        num = a*d+b*c
        dem = b*d
        def gcd(x,y):
            while y!=0:
                x,y=y,x%y
            return x
        g = gcd(num,dem)
        num = num //g
        dem = dem //g
    
        return str(num) +"/"+ str(dem) 

obj =Solution()
print(obj.add_fraction(1,2,3,4))