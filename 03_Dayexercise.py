#03Dayexercise
import math
#Número 1
Age=int('18')
#Número 2
Height=float('1.73')
#Número 3
Numcomplex=complex('3255')
# Número 4
base=int (input('Enter base: '))
height=int (input('Enter height: '))
area= int (0.5*base*height) 
print('The area of the triangle is: ', area)
#Número 5
sideA=int (input('Enter side A: '))
sideB=int (input('Enter side B: '))
sideC= int (input('Enter sideC: ')) 
perimeter=int(sideA+sideB+sideC)
print('The perimeter of the triangle is: ', perimeter)

#Número6
length=int (input('Enter length: '))
width=int (input('Enter width: '))
areaR= int (length*width)
print('The area of the rectangle is: ', areaR)
length=int (input('Enter length: '))
width=int (input('Enter width: '))
perimeterR= (2*(length+width))
print('The perimeter of the triangle is: ', perimeterR)

#Número7
radio=int (input('Enter radio: '))
pi=int(3.146)
areaC= int (pi*radio*radio)
print('The area of the circle is: ', areaC)
radio=int (input('Enter radio: '))
pi=int (3.1416)
circunference= (2*pi*radio)
print('The circunference of the circle is: ', circunference)
#Número 8 
x=input('Enter x')
y=input('Enter y')
slope= ()
#Número9
x1 = float(input('Enter x1:'))
y1 = float(input('Enter y1:'))
x2 = float(input('Enter x2:'))
y2 = float(input('Enter y2:'))
slope = (y2 - y1) / (x2 - x1)
print('The slope is:', slope)
distancia =math.sqrt ((x2 - x1)**2 + (y2 - y1)**2)
print('The Euclidean distance is:', distancia)

#Número 10
#Número 11 
#Número19
num = input('num:')
if (num==10):
    print('The num is equal 10 ')
else: "The num is different to 10"