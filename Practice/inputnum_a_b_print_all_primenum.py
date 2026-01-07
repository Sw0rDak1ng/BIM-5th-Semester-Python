a=int(input("Enter a:"))
b=int(input("Enter b:"))
for n in range(a,b+1):
    if n>1:
        count=0
        for i in range(1,n+1):
            if n%i==0:
                count+=1
        if count==2:
            print(n)
