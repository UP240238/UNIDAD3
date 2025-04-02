#03Dayexercise
import math
#Número 1 Declare your age as integer variable
Age=int('18')
#Número 2 Declare your height as a float variable
Height=float('1.73')
#Número 3 Declare a variable that store a complex number
Numcomplex=complex('3255')
# Número 4 Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
base=int (input('Enter base: '))
height=int (input('Enter height: '))
area= int (0.5*base*height) 
print('The area of the triangle is: ', area)
#Número 5 Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
sideA=int (input('Enter side A: '))
sideB=int (input('Enter side B: '))
sideC= int (input('Enter sideC: ')) 
perimeter=int(sideA+sideB+sideC)
print('The perimeter of the triangle is: ', perimeter)

#Número6 Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
length=int (input('Enter length: '))
width=int (input('Enter width: '))
areaR= int (length*width)
print('The area of the rectangle is: ', areaR)
length=int (input('Enter length: '))
width=int (input('Enter width: '))
perimeterR= (2*(length+width))
print('The perimeter of the triangle is: ', perimeterR)

#Número7 Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
radio=int (input('Enter radio: '))
pi=int(3.146)
areaC= int (pi*radio*radio)
print('The area of the circle is: ', areaC)
radio=int (input('Enter radio: '))
pi=int (3.1416)
circunference= (2*pi*radio)
print('The circunference of the circle is: ', circunference)
#Número 8 Calculate the slope, x-intercept and y-intercept of y = 2x -2
slope = 2  
y_intercept = -2  
x_intercept = -y_intercept / slope  
print(f"Pendiente: {slope}")
print(f"Intersección con el eje y: (0, {y_intercept})")
print(f"Intersección con el eje x: ({x_intercept}, 0)")
#Número9 Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
x1 = float(input('Enter x1:'))
y1 = float(input('Enter y1:'))
x2 = float(input('Enter x2:'))
y2 = float(input('Enter y2:'))
slope = (y2 - y1) / (x2 - x1)
print('The slope is:', slope)
distancia =math.sqrt ((x2 - x1)**2 + (y2 - y1)**2)
print('The Euclidean distance is:', distancia)
#Número 10 Compare the slopes in tasks 8 and 9.
#Número 11 Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
x = -3 
y = x**2 + 6*x + 9  
es_cero = (y == 0)  
es_negativo = (x < 0)  
es_no_positivo = not (y > 0) 
print("y es 0:", es_cero and "Sí" or "No")
print("x es negativo:", es_negativo and "Sí" or "No")
print("y NO es positivo:", es_no_positivo and "Sí" or "No")
#Número 12 Find the length of 'python' and 'dragon' and make a falsy comparison statement.
python = len('python')
dragon = len('dragon')
falsy_comparison = python > dragon and python < dragon  
#Número 13 Use and operator to check if 'on' is found in both 'python' and 'dragon'
on='on'in 'python'and 'on' in 'dragon'
#Número 14 I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
texto='I hope this course is not full of jargon'
jargon= 'jargon'in texto 
#Número 15 There is no 'on' in both dragon and python
on=not ('on'in 'python'and 'on' in 'dragon')
#Número 16 Find the length of the text python and convert the value to float and convert it to string
python = len('python')
python_float=float(python)
python_str=str(python_float)
#Número 17 Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
num=int(input('Ingresa el número'))
print(num % 2 == 0)
#Número 18 Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
division_floor=(7//3)==int(2.7)
#Número19 Check if type of '10' is equal to type of 10
num = input('num:')
if (num==10):
    print('The num is equal 10 ')
else: "The num is different to 10"
#Número 20 Check if int('9.8') is equal to 10
int=int(float('9.8'))==10 
#Número 21  Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
horas=float(input('Ingresa las horas '))
tarifa=float (input('Ingresa la trafia por hora'))
pago= horas* tarifa
print('Tu pago semanal es ', pago)
#Númerp 22  Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
Años=int(input('Ingresa cuantos años tienes : '))
Segundos_de_vida= Años*31557600
print('Has vivido por',Segundos_de_vida 'segundos')
#Número 23 Write a Python script that displays the following table
print(1,1,1,1,1)
print(2,1,2,4,8)
print(3,1,3,9,27)
print(4,1,4,16,64)
print(5,1,5,25,125)
