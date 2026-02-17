#wap to overload > than operator to compare two person object than contain name and age and display the details of elder person.

class person:
    def __init__(self,n,a):
        self.name=n
        self.age=a

    def __gt__(self,other):
        return self.age>other.age
    
p1=person('Ram',20)
p2=person('hari',21)
if p1>p2:
    print(p1.name,p1.age)
else:
    print(p2.name,p2.age)