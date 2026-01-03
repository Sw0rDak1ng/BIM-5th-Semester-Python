#Menu Driven Program 

print('-----Menu-----')
print('1.Area of circle')
print('2.Vowel or Consonant')
print('3.Odd or Even')

choice= int(input('Enter the choice(1-3):'))

if choice==1:
    r=float(input('Enter the radius of the circle:'))
    area=3.14*r*r
    print('The Radius of the circle is:',area)

elif choice==2:
    char=(input('Enter the Character:'))
    if char in ('aeiouAEIOU'):
        print(char,'is a vowel')
    else:
        print(char,'is a consonent')

elif choice==3:
    num=int(input('Enter the Number:'))
    if num%2==0:
        print(num,'is Even')
    else:
        print(num,'is Odd')
