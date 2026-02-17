# wap to overload + operator to add 2 distance objects that contains m and km.
class distance:
    def __init__(self,m,km):
        self.m=m
        self.km=km
    
    def __add__(self,other):
        m=self.m+other.m
        km=self.km+other.km//1000
        m=m%1000
        return distance(m,km)
d1=distance(500,2)
d2=distance(300,2)
d3=d2+d1
print(d3.m,d3.km)

''' operator with their magic method
+ = __add__(self,other)
- = __sub__(self,other)
* = __mul__(self,other)
/ = __truediv__(self,other)
// = __floordiv__(self,other)
** = __pow__(self,other)
>  =__gt__(self,other)
>=  =__ge__(self,other)
<  =__lt__(self,other)
<=  =__le__(self,other)
==  =__eq__(self,other)
!=  =__ne__(self,other)
'''