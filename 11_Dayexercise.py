#Exercise level 1 
#1Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def sumar_dos_numeros(a, b):
    return a + b

print(sumar_dos_numeros(3, 5)) 

#2Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle. 
import math

def area_de_circulo(r):
    return math.pi * r * r

print(area_de_circulo(5))  

#3Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
def sumar_todos_los_numeros(*args):
    if all(isinstance(arg, (int, float)) for arg in args):
        return sum(args)
    else:
        return "Error: Todos los elementos deben ser números."

print(sumar_todos_los_numeros(1, 2, 3)) 
print(sumar_todos_los_numeros(1, "dos", 3))  

#4Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
def convertir_celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32
print(convertir_celsius_a_fahrenheit(25)) 


#5 Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
def verificar_estacion(mes):
    estaciones = {
        "Diciembre": "Invierno", "Enero": "Invierno", "Febrero": "Invierno",
        "Marzo": "Primavera", "Abril": "Primavera", "Mayo": "Primavera",
        "Junio": "Verano", "Julio": "Verano", "Agosto": "Verano",
        "Septiembre": "Otoño", "Octubre": "Otoño", "Noviembre": "Otoño"
    }
    return estaciones.get(mes, "Mes no válido")

print(verificar_estacion("Marzo"))  

#6 Write a function called calculate_slope which return the slope of a linear equation
def calcular_pendiente(m, x1, y1, x2, y2):
    if x2 - x1 == 0:
        return "La pendiente es indefinida (línea vertical)."
    return (y2 - y1) / (x2 - x1)
print(calcular_pendiente(2, 1, 2, 3, 4)) 


#7 Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates
import math

def resolver_ecuacion_cuadratica(a, b, c):
    discriminante = b**2 - 4*a*c
    if discriminante > 0:
        raiz1 = (-b + math.sqrt(discriminante)) / (2 * a)
        raiz2 = (-b - math.sqrt(discriminante)) / (2 * a)
        return (raiz1, raiz2)
    elif discriminante == 0:
        raiz = -b / (2 * a)
        return (raiz,)
    else:
        return "No hay raíces reales"

print(resolver_ecuacion_cuadratica(1, -3, 2))  

#8 Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
def imprimir_lista(lst):
    for item in lst:
        print(item)

imprimir_lista([1, 2, 3])
#9 Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
def invertir_lista(lst):
    lista_invertida = []
    for i in range(len(lst)-1, -1, -1):
        lista_invertida.append(lst[i])
    return lista_invertida

print(invertir_lista([1, 2, 3, 4, 5]))  

#10 Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
def capitalizar_items_lista(lst):
    return [item.capitalize() for item in lst]

print(capitalizar_items_lista(["manzana", "banana", "cereza"]))  
#11 Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
def agregar_item(lst, item):
    lst.append(item)
    return lst
alimentos = ['Papas', 'Tomates', 'Mangos', 'Leche']
print(agregar_item(alimentos, 'Carne'))  
#12 Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
def eliminar_item(lst, item):
    if item in lst:
        lst.remove(item)
    else:
        return "El ítem no se encuentra en la lista."
    return lst
alimentos = ['Papas', 'Tomates', 'Mangos', 'Leche']
print(eliminar_item(alimentos, 'Mangos'))  
#13Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
def suma_de_numeros(n):
    return sum(range(1, n + 1))
print(suma_de_numeros(5)) 

#14Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
def suma_de_impares(n):
    return sum(i for i in range(1, n + 1) if i % 2 != 0)
print(suma_de_impares(5))
#15 Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.
def suma_de_pares(n):
    return sum(i for i in range(1, n + 1) if i % 2 == 0)
print(suma_de_pares(5))

#Exercise level 2 
#1Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
def evens_and_odds(n):
    pares = 0
    impares = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            pares += 1
        else:
            impares += 1
    return f"El número de impares son {impares}. El número de pares son {pares}."

print(evens_and_odds(100))

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        resultado = 1
        for i in range(1, n + 1):
            resultado *= i
        return resultado

print(factorial(5))  

#2Call your function is_empty, it takes a parameter and it checks if it is empty or not
def is_empty(valor):
    if not valor:  
        return True
    return False

print(is_empty(""))  
print(is_empty([1, 2, 3])) 
#3Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).
#Media
def calcular_media(lista):
    return sum(lista) / len(lista) if len(lista) > 0 else 0

print(calcular_media([1, 2, 3, 4, 5]))  
#MEdiana
def calcular_mediana(lista):
    lista_ordenada = sorted(lista)
    longitud = len(lista_ordenada)
    if longitud % 2 == 0:
        return (lista_ordenada[longitud // 2 - 1] + lista_ordenada[longitud // 2]) / 2
    else:
        return lista_ordenada[longitud // 2]

print(calcular_mediana([1, 2, 3, 4, 5]))  
#Moda 
from collections import Counter

def calcular_moda(lista):
    contador = Counter(lista)
    moda = contador.most_common(1)
    return moda[0][0] if moda else None

print(calcular_moda([1, 2, 2, 3, 4]))  

#Rango 
def calcular_rango(lista):
    return max(lista) - min(lista)

print(calcular_rango([1, 2, 3, 4, 5]))  

#Varianza 
def calcular_varianza(lista):
    media = calcular_media(lista)
    varianza = sum((x - media) ** 2 for x in lista) / len(lista)
    return varianza

print(calcular_varianza([1, 2, 3, 4, 5]))  
#Desviación Estandar 
import math

def calcular_desviacion_estandar(lista):
    varianza = calcular_varianza(lista)
    return math.sqrt(varianza)

print(calcular_desviacion_estandar([1, 2, 3, 4, 5]))  

#Exercise level 3 
#1Write a function called is_prime, which checks if a number is prime.
def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print(es_primo(5))  
print(es_primo(10))  

#2Write a functions which checks if all items are unique in the list.
def son_todos_unicos(lista):
    return len(lista) == len(set(lista))

print(son_todos_unicos([1, 2, 3, 4, 5])) 
print(son_todos_unicos([1, 2, 2, 4, 5]))  
#3Write a function which checks if all the items of the list are of the same data type.
def son_todos_del_mismo_tipo(lista):
    return len(set(type(x) for x in lista)) == 1

print(son_todos_del_mismo_tipo([1, 2, 3, 4]))  
print(son_todos_del_mismo_tipo([1, "2", 3])) 

#4Write a function which check if provided variable is a valid python variable
import keyword

def es_variable_valida(var_nombre):
    if not var_nombre.isidentifier() or keyword.iskeyword(var_nombre):
        return False
    return True
print(es_variable_valida("mi_var")) 
print(es_variable_valida("1var")) 
print(es_variable_valida("def"))  
#5Go to the data folder and access the countries-data.py file.
import keyword

def es_variable_valida(var_nombre):
    if not var_nombre.isidentifier() or keyword.iskeyword(var_nombre):
        return False
    return True

print(es_variable_valida("mi_var"))
print(es_variable_valida("1var")) 
print(es_variable_valida("def"))  

def paises_mas_poblados():
    paises = {
        "China": 1400,
        "India": 1380,
        "EE.UU.": 332,
        "Indonesia": 276,
        "Pakistán": 231,
        "Brasil": 213,
        "Nigeria": 206,
        "Bangladesh": 166,
        "Rusia": 146,
        "México": 126
    }
    

    paises_ordenados = sorted(paises.items(), key=lambda x: x[1], reverse=True)
    return paises_ordenados[:10]  

print(paises_mas_poblados())

