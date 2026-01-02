print('1.Area of circle')
print('2.Vowel/Consonant')
print('3.Odd/Even')
choice=int(input('Enter your choice(1-3)'))
if choice==1:
    radius=float(input('Enter the radius of the circle'))
    area=3.14*radius*radius
    print('Area of the circle is:',area)

elif choice==2:
    char=input('Enter a character:')
    if char in 'AEIOUaeiou':
        print(char,'Vowel')



