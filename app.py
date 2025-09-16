#addition
'''
num1 = int(input("Enter a number:"))
num2 = int(input("Enter a number:"))

result = num1 + num2
print(f"Sum: {num1} + {num2} = {result}")

'''


#Division 
'''
um3 = int(input("Enter a number for division:"))
num4 = int(input("Enter a number for division: "))
if num4 == 0:
 print("Division of zero is not possible")
else:
 result = num3 / num4
 print(f"Division : {num3} / {num4} = {result}")
 
'''

#area of the triangle area = 0.5    (area * base * length)
'''
base = float(input("Enter a size for base:"))
length = float(input("Enter a length :"))
print(f"Base : {base} Length : {length}")
area = 0.5 * base * length
print(f" The area of the triangle is {area}")

'''


#swap 2 variables
'''
a = int(input(" Enter a number for a:"))
b = int(input("Enter a number for b:"))
print(f"Before: a = {a} b = {b}")
temp = a
a = b
b = temp
print(f"After: a = {a} b = {b}")

'''

#generate random numbers
'''
import random
print(f"Random Numbers: {random.randint(1,10)}")

'''

#kilometers to miles   1 kl = 0.621371 miles
'''
kilometers = float(input("Enter a distance: "))
conv = 0.621371 
miles = kilometers * conv
print(input(f"{kilometers} Kilometers is equal to {miles} Miles"))

'''

#celsius to fahrenheit (celsius * 9/5 ) + 32
'''
celsius = float(input("enter a temperature: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius} Celsius is equal to {fahrenheit} fahrenheit")

'''



#display calendar
'''
import calendar
year = int(input("Enter a Year: "))
month = int(input("Enter a Month: "))

cal = calendar.month(year, month)
print(cal)

'''


#solve quadratic equation 
# (ax** + bx + c = 0) 
# where a,b,c are real numbers and a /= 0
#
'''
import math

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

discriminant = b**2 - 4*a*c 
if discriminant > 0 :
  root1 = (-b + math.sqrt(discriminant)) / (2*a) 
  root2 = (-b - math.sqrt(discriminant)) / (2*a)
print(f"Root 1: {root1}")
print(f"Root 2: {root2}")
'''




#swap 2 variables without temp
'''
x = int(input("Enter a number for x: "))
y = int(input("Enter a number for y: "))

print(f" Before: x:{x} y: {y}")

x,y = y,x
print(f" after: x: {x} y: {y}")

'''



#check if number is negative,positive, zero
#check if number is odd,even
#check leap year 
#check prime number
#print all prime numbers in interval of 1-10
#find the factorial of a number
#display multiplication number
#print the fibonacci sequence
#check armstrong numbers
#find armstrong numbers interval
#find the sum of natural numbers
#largest among three numbers
#find the factorial using recursion
#program to reverse a string
#check palindrome string  
#calculate the sum of digits of a number
#find the maximum and minimum of the list
#sort a list
#find the largest element of a list
#count the number of vowels in a string
#find the length of a string without using len()
#
#
#
#
#
#
#
#