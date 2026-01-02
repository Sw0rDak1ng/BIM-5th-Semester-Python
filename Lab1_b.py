import math

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

x = math.sqrt(a)
y = math.sqrt(b)

print("Square root of", a, "is", x)
print("Square root of", b, "is", y)

s = x + y
print("Sum of the square roots is", s)
