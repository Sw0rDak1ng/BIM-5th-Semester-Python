#Create a menu driven program
print('1.Area of circle')
print('2.Vowel/Consonent')
print('3.Odd/Even')
choice=int(input('Enter your choice:'))
if choice==1:
    radius=float(input('Enter the radius of the circle:'))
    area=3.14*radius*radius
    print('Area of the circle is:',area)

elif choice==2:
    char=input('Enter a character:')
    if char in 'AEIOUaeiou':
        print('Vowel')
    else:
        print('consonent')

elif choice==3:
    a=int(input('Enter a number:'))
    if a%2==0:
        print('Even')
    else:
        print('odd')



