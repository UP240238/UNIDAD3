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
slope = 2  
y_intercept = -2  
x_intercept = -y_intercept / slope  
print(f"Pendiente: {slope}")
print(f"Intersección con el eje y: (0, {y_intercept})")
print(f"Intersección con el eje x: ({x_intercept}, 0)")
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
x = -3 
y = x**2 + 6*x + 9  
es_cero = (y == 0)  
es_negativo = (x < 0)  
es_no_positivo = not (y > 0) 
print("y es 0:", es_cero and "Sí" or "No")
print("x es negativo:", es_negativo and "Sí" or "No")
print("y NO es positivo:", es_no_positivo and "Sí" or "No")
#Número 12
python = len('python')
dragon = len('dragon')
falsy_comparison = python > dragon and python < dragon  
#Número 13 
on='on'in 'python'and 'on' in 'dragon'
#Número 14 
texto='I hope this course is not full of jargon'
jargon= 'jargon'in texto 
#Número 15 
on=not ('on'in 'python'and 'on' in 'dragon')
#Número 16
python = len('python')
python_float=float(python)
python_str=str(python_float)
#Número 17 
num=int(input('Ingresa el número'))
print(num % 2 == 0)
#Número 18 
division_floor=(7//3)==int(2.7)
#Número19
num = input('num:')
if (num==10):
    print('The num is equal 10 ')
else: "The num is different to 10"
#Número 20
int=int(float('9.8'))==10 
#Número 21 
horas=float(input('Ingresa las horas '))
tarifa=float (input('Ingresa la trafia por hora'))
pago= horas* tarifa
print('Tu pago semanal es ', pago)
#Númerp 22 
Años=int(input('Ingresa cuantos años tienes : '))
Segundos_de_vida= Años*31557600
print('Has vivido por',Segundos_de_vida 'segundos')
#Número 23 
print(1,1,1,1,1)
print(2,1,2,4,8)
print(3,1,3,9,27)
print(4,1,4,16,64)
print(5,1,5,25,125)
